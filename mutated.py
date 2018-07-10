import pandas as pd

def mutatedGenesFiles(mutatedGenes):

	pathName1 = input("Enter the path of first csv file:") 
	pathName2 = input("Enter the path of second csv file:")
	
	output1 = input("Desired name of the first output file:")
	output2 = input("Desired name of the second output file:")
					
	file1 = pd.read_csv(pathName1)		#the .csv files are read and the values are stored in data frames
	file2 = pd.read_csv(pathName2)
	
	columns1 = list(file1)		#a list of columns of file1 data fram is stored in columns1
	columns2 = list(file2)  	#similarly for columns2
	
	mutatedFile1 = pd.DataFrame(columns = columns1)		 #initializing data frame to store information about mutated genes in first type of cancer
	mutatedFile2 = pd.DataFrame(columns = columns2) 	#initializing data frame to store information about mutated genes in second type of cancer

	for indexes,rows in file1.iterrows(): 			#storing information of mutated genes of first type of cancer in mutatedFile1
		if rows['GenomicIdentifier'] in mutatedGenes:
			mutatedFile1.loc[file1.index[indexes]] = file1.loc[indexes]
	
	for indexes, rows in file2.iterrows():   		#storing information of mutated genes of second type of cancer in mutatedFile2
		if rows['GenomicIdentifier'] in mutatedGenes:
			mutatedFile2.loc[file2.index[indexes]] = file2.loc[indexes]
	
	mutatedFile1.to_csv(output1, index = False)   #storing dataframes as .csv files
	mutatedFile2.to_csv(output2, index = False)
	
	

mutatedGenesFiles([]) #the array containing the mutated GenomicIdentifiers should be passed to this function
