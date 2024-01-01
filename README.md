# LoadClusterScheduler

## Summary
This is a command line tool that uses the KMeans and MeanShift from sklearn to cluster data in a specified cell range in an xlsx document.  It outputs a timestamped "cluster report" folder to the desktop containing a .csv file with the user input and labels and a visualization plot if the number of features is less than 3. 

## Use Case
This tool was meant to aid in developing construction schedules in my day-to-day workflow as a structural engineer. 

Scenario: Imagine you have 100 columns in a building under various compressive and possibly lateral forces. Some columns have a lot of force on them and need to be large, while others have smaller forces and can be significantly smaller. We need to choose column sizes for the project to give to a contractor, but they must be large enough to withstand the load applied to them. One extreme would be to take the largest load, size a very large column, and specify that for all the columns in the building. However, this is inefficient because most columns do not need to be that large and can be made smaller to save material and money. On the other hand, specifying different column sizes for each load, while efficient material-wise, is very tedious for a contractor to build and error-prone. Enter the LoadClusterScheduler tool: This tool groups columns with similar loads into clusters, allowing for efficient material usage while not providing too many options.



## Set Up
The source code can be downloaded and used with an interpreter. However, executables are provided for those wanting to run the application without installing python and an IDE.

## Usage
To run the application from the command line, enter the path to the downloaded executable and the required arguments (xlsx file path and cell range). Note cell range must be imputed in typical excel fashion (“sheet_name:A1:C30” or “sheet_name!A1:C20,H,L” for multiple columns). 

``` path/to/executable <path/to/xlsx_file> <cell_range> ```

Additionally, the application expects the user to include an ID column as the first column in the cell range. This column will be dropped for analysis but is utilized in the output report for clarity. In the image below, only the features to the right of ID will be clustered. 



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




