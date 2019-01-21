import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
	print("Program: CSV Header Cleaning")
	print("Release: 1.1.1")
	print("Date: 2019-01-21")
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

	#Ask for delimination
	delimination = input("Enter Deliminator: ")
	
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

	encode_index = 0
	encoders = ["utf8", "utf16", "latin_1", "ascii"]
	while delete_header(file_in, file_out, number_of_columns, delimination, encoders[encode_index]) == "Encode Error":
		if encode_index < len(encoders) - 1:
			encode_index = encode_index + 1
		else:
			print("Can't find appropriate encoder")
			exit()

	print()
	print("Program Completed!")
	print("New file saved at: " + file_out)
	input("Press Enter to close")

def delete_header(file_in, file_out, number_of_columns, delimination, encoding):
	try:
		with open(r'' + file_in, 'r', encoding=encoding) as f_input, open(r'' + file_out, 'w', encoding=encoding,
																		  newline='') as f_output:
			print("Encoder Used: " + encoding)

			# Set input reader
			csv_input = csv.reader(f_input, delimiter=str(delimination), quotechar='"')

			# Set output writer
			csv_output = csv.writer(f_output, delimiter=',', quotechar='"')

			# Set header scan required to 1
			header_scan = 1

			# Each each row
			for row in csv_input:

				# Try to read the row at specified column
				try:
					if header_scan == 1:
						row[number_of_columns - 1]
						header_scan = 0

					# Write row if it can read
					csv_output.writerow(row)

				# If it can't read at specified column, skip row by doing nothing to it.
				except:
					pass
	except UnicodeDecodeError:
		print("Encoder error for " + encoding)
		print()
		return "Encode Error"

	return csv_output

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
