import pandas as pd
from pathlib import Path

def mergeCsv():
	inputPath1 = Path(input("Enter the file path of the first csv file:"))	#Asking the user to input the file paths of the .csv files
	inputPath2 = Path(input("Enter the file path of the second csv file:"))
	
	outputFile = Path(input("Enter the name of the output file:"))	#Asking the user to enter the name of the output file

	firstData = pd.read_csv(inputPath1)	#Reading .csv files' data into dataframes
	secondData = pd.read_csv(inputPath2)
								
	firstData.set_index("GenomicIdentifier")	#setting the index of the data frames to GenomicIdentifier
	secondData.set_index("GenomicIdentifier")
	
	firstData = firstData.T			#transposing data frames
	secondData = secondData.T
						
	firstData.append(secondData)		#appending the second data frame to the first data frame
							
	firstData.to_csv(outputFile, index = False)	#converting the merged dataframe into a .csv file

mergeCsv()

