# LoadClusterScheduler

![Jan-01-2024 13-28-44](https://github.com/akpax/LoadClusterScheduler/assets/78048703/49dd906f-96cf-4455-959e-a0c79fc24c7c)



## Summary
This is a command line tool that uses the KMeans and MeanShift from sklearn to cluster data in a specified cell range in an xlsx document.  It outputs a timestamped "cluster report" folder to the desktop containing a .csv file with the user input and labels and a visualization plot if the number of features is less than 3. 


## Set Up
The source code can be downloaded and used with an interpreter. However, executables are provided for those wanting to run the application without installing python and an IDE.


## Usage
To run the application from the command line, enter the path to the downloaded executable and the required arguments (xlsx file path and cell range). Note cell range must be imputed in typical excel fashion (“sheet_name:A1:C30” or “sheet_name!A1:C20,H,L” for multiple columns). 

``` path/to/executable <path/to/xlsx_file> <cell_range> ```

Additionally, the application expects the user to include an ID column as the first column in the cell range. This column will be dropped for analysis but is utilized in the output report for clarity. In the image below, only the features to the right of ID will be clustered. 

![Screenshot 2024-01-01 at 1 00 41 PM](https://github.com/akpax/LoadClusterScheduler/assets/78048703/d36f1dc4-03b1-45d9-b0a4-2453fd431958)



## Simplifying Command Line Usage with Aliases and Batch Files
To make running LoadClusterScheduler more convenient from the command line, you can create shortcuts. In Linux, this is done by setting up an 'alias', and in Windows, by creating a '.bat' (batch) file. These shortcuts allow you to run the application without typing the full path to the executable every time.


### In Linux:
An alias is a shorthand command that references another command. It's a way to customize your command line experience by creating simple, memorable commands to execute longer or more complex command lines. Once an alias is set up, you only need to type the alias name instead of the full command.


1. Open .bashrc or .zshrc file in terminal
```
nano .zshrc
 ```

2. Add alias
```
 alias cluster=’absolute/path/to/executable'
 ```

3. Save and exit editor

4. Restart terminal
```
source ~/.bashrc
 ```

5. Now we can run the executable using 

``` cluster <path/to/file> <sheet_range> [cluster_quantity] ```


### In Windows:
A batch file (with a .bat extension) is a script file in DOS, Windows, and OS/2 operating systems. It consists of a series of commands to be executed by the command-line interpreter. Creating a .bat file for LoadClusterScheduler will allow you to start the application by typing a short command instead of the full path to the executable. 
1. Create a .bat file with the following information:
```
@echo off
REM Path to your executable
set EXECUTABLE_PATH=C:\path\to\your_executable.exe

REM Running the executable
"%EXECUTABLE_PATH%" %*
```

2. Name .bat file cluster.bat for convenience and save to a directory that is included in the system’s PATH 

3. Now we can run the executable using 

``` cluster.bat <path/to/file> <sheet_range> [cluster_quantity] ```


## Use Case
This tool was initially developed to aid in constructing schedules in my daily workflow as a structural engineer. However, it is versatile and not industry-specific, with additional possible use cases including:

* Retail Inventory Management: Clustering products based on factors such as sales volume, seasonality, and customer preferences.
* Customer Segmentation for Marketing: Identifying distinct customer groups for targeted marketing strategies.
* Real Estate Market Analysis: Clustering properties based on attributes like size, price, and amenities.
* Sports Analytics: Grouping player performances based on key metrics.


## Why This Tool Helps Me as a Structural Engineer
Scenario: Imagine a building with 100 columns, each subjected to various compressive and possibly lateral forces. Some columns bear significant forces and thus need to be large, whereas others endure smaller forces and can be substantially smaller. Selecting appropriate column sizes for a project is essential, ensuring each column is robust enough to handle the applied load.

One approach is to size all columns in the building to withstand the maximum load, which results in uniformly large columns. While this method ensures structural integrity, it is materially inefficient and costly. Conversely, custom-sizing each column for its specific load, though materially efficient, leads to an overly complicated design. This complexity is not only tedious but also prone to errors when built by contractors. The LoadClusterScheduler tool addresses this dilemma by grouping columns with similar loads into clusters. This approach strikes a balance between material efficiency and practicality, offering a manageable number of options. It enables engineers to concentrate on core engineering tasks, streamlining the complexity of column grouping into a user-friendly command-line tool.
