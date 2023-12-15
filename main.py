from excel_input_parser import ExcelInputParser
from cluster_visualizer import ClusterVisualizer
import pandas as pd
from sklearn.cluster import KMeans, MeanShift
import os
from datetime import datetime

import matplotlib as plt 
file_path = "/Users/austinpaxton/Documents/ML_projects/LoadClusterScheduler/test_files/Pier Loads.xlsx"
user_input = "Pier Load Summary!A29:D50"
user_cluster_qty= None

parser = ExcelInputParser()
parser.parse_input(user_input)

# Extract necessary arguments
sheet_name = parser.sheet_name
usecols = parser.extract_usecols()
skiprows, nrows = parser.extract_rows()

df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=usecols, skiprows=skiprows, nrows=nrows)
print(df.tail())


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
    
X = format_data_for_training(df)

print(X.head())
# pick model based on wether user specified cluster quantity
if not user_cluster_qty:
    model = MeanShift()
else:
    model = KMeans()
    
# fit model and update user_input dataframe
model.fit(X)
labels = model.labels_
df["labels"] = model.labels_
df = df.sort_values(by="labels",ascending=True)
centers = model.cluster_centers_
# print(df.head())

# create folder for report using current date and time
date = datetime.now()
formated_date = date.strftime("%d-%m-%Y_%H:%M:%S")
home_directory = os.path.expanduser("~") # get Home directory
folder_name = f"cluster_report_{formated_date}"
output_folder_path = os.path.join(home_directory,"Desktop",folder_name)
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)
    
# output user dataframe w results to .csv in report folder
csv_path = os.path.join(output_folder_path, "user_input&results.csv")
df.to_csv(csv_path, index=False)

# plot results
cluster_visualizer = ClusterVisualizer()
cluster_visualizer.set_data(data=X, labels=labels, centers=centers)
cluster_visualizer.plot(output_folder_path)

