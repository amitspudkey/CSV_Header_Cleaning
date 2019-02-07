# BN_CSV_Header_Cleaning
A small standalone program that removes report headers from CSV's.

The program operates by scanning a csv file on a given column until it sees data, then deletes the rows above that location.


________________________________________________________________________________________________________________________________________
Example:

This is an example of a report

Date 02/07/2019

Column 1, Column 2, Column 3, Column 4, Column 5

Data 1, Data 2, Data 3, Data 4, Data 5

Data 1, Data 2, Data 3, Data 4, Data 5
________________________________________________________________________________________________________________________________________



Step 1: Start the program.

Step 2: Enter Deliminator: 

    The program will ask and ask for the Deliminator of the file.
    
Step 3: Please enter the number of columns for the search:

    The program is asking for a column number to scan down to determine the header.
    
    In the example report, the header data is held within the first column.  
    
    Any number greater than 1 and less than the total number of columns would work. 
    
 Step 4: Select input file using the dialog box.
 
 Step 5: Create a output file using the dialog box.
