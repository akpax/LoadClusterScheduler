from excel_input_parser import ExcelInputParser
from cluster_visualizer import ClusterVisualizer
import pandas as pd
from sklearn.cluster import KMeans, MeanShift
import os
from datetime import datetime
import matplotlib as plt 
import tkinter as tk
from argparse import ArgumentParser
from icecream import ic


# arg_parser = ArgumentParser()

# arg_parser.add_argument("xlsx_path", help="Path to .xlsx file to be analyzed", type=str)
# arg_parser.add_argument("cell_range", help="Cell range of data to be analyzed formated as 'sheetname!A3:D10'", type=str)
# arg_parser.add_argument("--cluster_qty", help="use this argument to enter desired number of clusters", type=int)

# args = arg_parser.parse_args()
# xlsx_path = args.xlsx_path
# cell_range = args.cell_range
# cluster_qty = args.cluster_qty
# ic(xlsx_path)
# ic(cell_range)
# ic(cluster_qty)
# ###################################### tkinter entry for demo #################################################
# window = tk.Tk()
# tk.Label(window, text="Excel Path").grid(row=0)
# tk.Label(window, text="Cell Range").grid(row=1)
# tk.Label(window, text="Specify Desired Clusters (optional)").grid(row=2)

# excel_path = tk.Entry(window)
# cell_range = tk.Entry(window)
# cluster_qty = tk.Entry(window)

# excel_path.grid(row=0, column=1)
# cell_range.grid(row=1, column=1)
# cluster_qty.grid(row=2, column=1)

# tk.Button(window, text="Analyze", command=window.quit).grid(row=3, column=1)

# tk.mainloop()

# #get inputs from tkinter
# file_path = excel_path.get()
# user_input = cell_range.get()
# user_cluster_qty = cluster_qty.get()
# print(type(user_cluster_qty))

###################################### Inputs #################################################
file_path = "/Users/austinpaxton/Documents/ML_projects/LoadClusterScheduler/test_files/Pier Loads.xlsx"
user_input = "Pier Load Summary!A29:C50"
user_cluster_qty= 3

###################################### Functions #################################################
def format_data_for_training(X):
    """
    Removes label column of dataframe to form dataset
    """
    if len(X.shape) == 1:
        # keep type as pandas df
        return X.iloc[:,[1]]
    else:
        # If 2D or 3D, return as is
        return X.iloc[:,1:]

def append_date_and_time(prefix):
    date = datetime.now()
    formated_date = date.strftime("%m-%d-%Y_%H:%M:%S")
    return f"{prefix}_{formated_date}"

# create folder for report using current date and time
def create_output_folder_path(name):
    """
    Finds desktop path and returns output folder path inside desktop dir
    """
    # date = datetime.now()
    # formated_date = date.strftime("%d-%m-%Y_%H:%M:%S")
    folder_name = append_date_and_time(name)
    home_directory = os.path.expanduser("~") # get Home directory
    output_folder_path = os.path.join(home_directory,"Desktop",folder_name)
    return output_folder_path

if __name__ == "__main__":
    parser = ExcelInputParser()
    parser.parse_input(user_input)

    # Extract necessary arguments for pd.read_excel
    sheet_name = parser.sheet_name
    usecols = parser.extract_usecols()
    skiprows, nrows = parser.extract_rows()
    ic(skiprows)
    ic(nrows)
    ic(usecols)
    ic(sheet_name)
    df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=usecols, skiprows=skiprows, nrows=nrows)
    print(df.tail())

        
    X = format_data_for_training(df)

    print(X.head())
    # pick model based on wether user specified cluster quantity
    if not user_cluster_qty:
        model = MeanShift()
        print("MODEL: MeanShift")
    else:
        model = KMeans(int(user_cluster_qty))
        print("MODEL: KMeans")
        
    # fit model and update user_input dataframe
    model.fit(X)
    labels = model.labels_
    df["labels"] = model.labels_
    df = df.sort_values(by="labels",ascending=True)
    centers = model.cluster_centers_


    output_folder_path = create_output_folder_path("cluster_report")

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
        
    # output user dataframe w results to .csv in report folder
    csv_path = os.path.join(output_folder_path, "user_input&results.csv")
    df.to_csv(csv_path, index=False)

    # plot results and output to output folder
    cluster_visualizer = ClusterVisualizer()
    cluster_visualizer.set_data(data=X, labels=labels, centers=centers)
    cluster_visualizer.plot(output_folder_path)

