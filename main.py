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


###################################### Inputs #################################################
# xlsx_path = "/Users/austinpaxton/Documents/ML_projects/LoadClusterScheduler/test_files/Pier Loads.xlsx"
# cell_range = "Pier Load Summary!A29:C50"
# cluster_qty= None

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
    # use arg_parser to recieve command line args
    arg_parser = ArgumentParser()

    arg_parser.add_argument("xlsx_path", help="Path to .xlsx file to be analyzed", type=str)
    arg_parser.add_argument("cell_range", help="Cell range of data to be analyzed formated as 'sheetname!A3:D10'", type=str)
    arg_parser.add_argument("--cluster_qty", help="use this argument to enter desired number of clusters", type=int)

    args = arg_parser.parse_args()
    xlsx_path = args.xlsx_path
    cell_range = args.cell_range
    cluster_qty = args.cluster_qty

    print("__________________________User Inputs Recieved________________________")
    print(f"{xlsx_path=}")
    print(f"{cell_range=}")
    print(f"{cluster_qty=}\n")
    parser = ExcelInputParser()
    parser.parse_input(cell_range)

    # Extract necessary arguments for pd.read_excel
    sheet_name = parser.sheet_name
    usecols = parser.extract_usecols()
    skiprows, nrows = parser.extract_rows()
    
    df = pd.read_excel(xlsx_path, sheet_name=sheet_name, usecols=usecols, skiprows=skiprows, nrows=nrows)
    print("__________________________Data Loaded________________________")
    print(f"- Number of Entries: {len(df)}")
    print("- User Inputed Data:")
    print(df)
    print("\n")
        
    X = format_data_for_training(df)
    print("- Data to be Analyzed:")
    print(X)
    print("\n")

    
    # pick model based on wether user specified cluster quantity
    print("__________________________Determine Analysis Method Based on User-Defined CLuster Quantity________________________")
    if not cluster_qty:
        model = MeanShift()
        print("- MODEL: MeanShift \n")
    else:
        model = KMeans(int(cluster_qty))
        print("- MODEL: KMeans \n")
        
    # fit model and update cell_range dataframe
    print("__________________________Analyze Data________________________")
    model.fit(X)
    labels = model.labels_
    df["labels"] = model.labels_
    df = df.sort_values(by="labels",ascending=True)
    print(f"- Labeled Dataframe: ")
    print(df)
    print("\n")
    centers = model.cluster_centers_

    print("__________________________Create Cluster Report________________________")
    output_folder_path = create_output_folder_path("cluster_report")
    print(f"- Output Folder: {output_folder_path}")

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
        print("     * Folder created *")
        
    # output user dataframe w results to .csv in report folder
    csv_path = os.path.join(output_folder_path, "cell_range&results.csv")
    df.to_csv(csv_path, index=False)
    print("     * .csv Outputed Successfully *")

    # plot results and output to output folder
    cluster_visualizer = ClusterVisualizer()
    cluster_visualizer.set_data(data=X, labels=labels, centers=centers)
    cluster_visualizer.plot(output_folder_path)
    print("     * Plot Outputed Successfully *")

