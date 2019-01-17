import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
	print("Program: CSV Header Cleaning")
	print("Release: 1.0")
	print("Date: 2019-01-17")
	print("Author: Brian Neely")
	print()
	print()
	print("This program reads a csv file and will delete the first rows that do not have specified column.")
	print("This is typically, because of a report header")
	print("To use, specify a number of columns that would be longer than a report header.")
	print("While, ensuring that the number of columns is less than or equal to the number of columns of csv.")
	print("Specify the location of the csv.")
	print("Specify the save location and filename.")
	print()
	print()
	
	#Hide Tkinter GUI
	Tk().withdraw()
	
	#Ask for number of columns
	number_of_columns = number_of_columns_input()
	
	#Find input file
	file_in = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Comma Separated Values","*.csv"),("all files","*.*")))
	if not file_in:
		input("Program Terminated. Press Enter to continue...")
		exit()

	#Set ouput file
	file_out = asksaveasfilename(initialdir = file_in,title = "Select file",filetypes = (("Comma Separated Values","*.csv"),("all files","*.*")))
	if not file_out:
		input("Program Terminated. Press Enter to continue...")
		exit()

	#Create an empty output file
	open(file_out, 'a').close()
	
	#Open input and output files. Define as utf8
	with open(r'' + file_in, 'r', encoding="utf8") as f_input, open(r'' + file_out, 'w', encoding="utf8", newline='') as f_output:
		print()
		
		#Set input reader
		csv_input = csv.reader(f_input, delimiter=',', quotechar='"')
		
		#Set output writer
		csv_output = csv.writer(f_output, delimiter=',', quotechar='"')

		#Set header scan required to 1
		header_scan = 1
		
		#Each each row
		for row in csv_input:
			
			#Try to read the row at specified column
			try: 
				if header_scan == 1:
					row[number_of_columns - 1]
					header_scan = 0
				
				#Write row if it can read
				csv_output.writerow(row)
				
			#If it can't read at specified column, skip row by doing nothing to it.
			except:
				print("Deleting line")

	print("Program Completed!")
	print("New file saved at: " + file_out)
	input("Press Enter to close")

def number_of_columns_input() -> int:
	while True:
		initial = input("Please enter the number of columns for the search: ")
		try:
			columns = int(initial)
			if columns > 0:
				break
			else:
				print("Input only accepts positive integer numbers.")
		except ValueError:
			print("Input only accepts positive integer numbers.")
	return columns


if __name__ == '__main__':
	main()
