import pandas as pd
from pathlib import Path

def mutatedGenesFiles(mutatedGenes):

	pathName1 = Path(input("Enter the path of first csv file:")) 
	pathName2 = Path(input("Enter the path of second csv file:"))
	
	output1 = input("Desired name of the first output file:")
	output2 = input("Desired name of the second output file:")
					
	print("Copying values from files into data frames.....")
	
	file1 = pd.read_csv(pathName1)		#the .csv files are read and the values are stored in data frames
	file2 = pd.read_csv(pathName2)
	
	print("Copying data done.")

	print("Creating data frames to store mutated genes' info.....")
	
	columns1 = list(file1)		#a list of columns of file1 data fram is stored in columns1
	columns2 = list(file2)  	#similarly for columns2
	
	mutatedFile1 = pd.DataFrame(columns = columns1)		 #initializing data frame to store information about mutated genes in first type of cancer
	mutatedFile2 = pd.DataFrame(columns = columns2) 	#initializing data frame to store information about mutated genes in second type of cancer
	
	print("Initialization done.")
	
	print("Storing mutated genes' info in the first data frame.....")
	
	for indexes,rows in file1.iterrows(): 			#storing information of mutated genes of first type of cancer in mutatedFile1
		if rows['GenomicIdentifier'] in mutatedGenes:
			mutatedFile1.loc[file1.index[indexes]] = file1.loc[indexes]
	
	print("Done for the first data frame.")
	
	print("Storing started for second data frame......")
	
	for indexes, rows in file2.iterrows():   		#storing information of mutated genes of second type of cancer in mutatedFile2
		if rows['GenomicIdentifier'] in mutatedGenes:
			mutatedFile2.loc[file2.index[indexes]] = file2.loc[indexes]
	
	print("Done for the second data frame.")

	print("Converting data frames to .csv files.....")
	
	mutatedFile1.to_csv(output1, index = False)   #storing dataframes as .csv files
	mutatedFile2.to_csv(output2, index = False)
	
	print("Completed 100%")
	

mutatedGenesFiles(['ENSG00000217769.4', 'ENSG00000266206.1', 'ENSG00000241604.3', 'ENSG00000259086.3', 'ENSG00000243095.1', 'ENSG00000263426.2', 'ENSG00000235166.6', 'ENSG00000278997.1', 'ENSG00000273006.1', 'ENSG00000271456.1', 'ENSG00000267184.1', 'ENSG00000207951.1', 'ENSG00000115596.3', 'ENSG00000222281.1', 'ENSG00000264696.1', 'ENSG00000222721.1', 'ENSG00000273987.1', 'ENSG00000196139.10', 'ENSG00000261304.1', 'ENSG00000233994.2', 'ENSG00000255469.1', 'ENSG00000184933.4', 'ENSG00000277062.1', 'ENSG00000279769.1', 'ENSG00000254792.1', 'ENSG00000116783.13', 'ENSG00000223890.1', 'ENSG00000223575.2', 'ENSG00000150527.15', 'ENSG00000236880.1', 'ENSG00000106571.11', 'ENSG00000273406.1', 'ENSG00000236082.2', 'ENSG00000261182.1', 'ENSG00000275215.1', 'ENSG00000220635.2', 'ENSG00000267335.2', 'ENSG00000254744.3', 'ENSG00000243828.2', 'ENSG00000227336.1', 'ENSG00000185955.4', 'ENSG00000279749.1', 'ENSG00000266827.1', 'ENSG00000258423.1', 'ENSG00000165874.11', 'ENSG00000168418.7', 'ENSG00000164821.4', 'ENSG00000188886.3', 'ENSG00000278455.1', 'ENSG00000107105.13']) #the array containing the mutated GenomicIdentifiers should be passed to this function
