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
	frames = [mutatedFile1, mutatedFile2]
	result = pd.concat(frames)
	result.to_csv('result.txt', index = False, sep = ' ', mode = 'a')
	print("Converting data frames to .csv files.....")
	
	mutatedFile1.to_csv(output1, index = False)   #storing dataframes as .csv files
	mutatedFile2.to_csv(output2, index = False)
	
	print("Completed 100%")
	

mutatedGenesFiles(['ENSG00000091490.9', 'ENSG00000229415.8', 'ENSG00000275410.3', 'ENSG00000268388.4', 'ENSG00000140563.13', 'ENSG00000254366.5', 'ENSG00000196188.9', 'ENSG00000136352.16', 'ENSG00000229807.8', 'ENSG00000206159.9', 'ENSG00000140297.11', 'ENSG00000136944.16', 'ENSG00000168631.10', 'ENSG00000156510.12', 'ENSG00000256802.2', 'ENSG00000068650.17', 'ENSG00000133661.14', 'ENSG00000121075.8', 'ENSG00000258844.1', 'ENSG00000240800.1', 'ENSG00000253563.2', 'ENSG00000183878.14', 'ENSG00000122852.13', 'ENSG00000107485.14', 'ENSG00000110484.6', 'ENSG00000154620.5', 'ENSG00000113494.15', 'ENSG00000237125.7', 'ENSG00000198189.9', 'ENSG00000260197.1', 'ENSG00000229847.7', 'ENSG00000218048.2', 'ENSG00000123977.8', 'ENSG00000241859.5', 'ENSG00000231535.4', 'ENSG00000225768.1', 'ENSG00000198113.2', 'ENSG00000163251.3', 'ENSG00000176728.6', 'ENSG00000275385.1', 'ENSG00000145113.20', 'ENSG00000152785.6', 'ENSG00000131400.6', 'ENSG00000257520.1', 'ENSG00000233070.1', 'ENSG00000259803.5', 'ENSG00000134215.14', 'ENSG00000259974.2', 'ENSG00000197308.7', 'ENSG00000114374.11', 'ENSG00000136153.18', 'ENSG00000179241.11', 'ENSG00000012817.14', 'ENSG00000118526.6', 'ENSG00000047936.9', 'ENSG00000233864.6', 'ENSG00000198488.9', 'ENSG00000280002.1', 'ENSG00000164266.9', 'ENSG00000224842.2', 'ENSG00000167105.6', 'ENSG00000168878.15', 'ENSG00000115468.10', 'ENSG00000136155.15', 'ENSG00000124935.3', 'ENSG00000164107.8', 'ENSG00000235687.7', 'ENSG00000170370.11', 'ENSG00000123838.9', 'ENSG00000183434.9', 'ENSG00000080293.8', 'ENSG00000104447.10', 'ENSG00000243350.1', 'ENSG00000099725.13', 'ENSG00000125798.13', 'ENSG00000278847.1', 'ENSG00000165246.11', 'ENSG00000198692.8', 'ENSG00000114455.12', 'ENSG00000067646.10', 'ENSG00000163064.6', 'ENSG00000125845.6', 'ENSG00000131002.10', 'ENSG00000236313.1', 'ENSG00000129824.14', 'ENSG00000171560.13', 'ENSG00000146166.15', 'ENSG00000215580.9', 'ENSG00000148513.16', 'ENSG00000168484.11', 'ENSG00000103241.6', 'ENSG00000067048.15', 'ENSG00000214313.7', 'ENSG00000198183.10', 'ENSG00000234918.1', 'ENSG00000137203.9', 'ENSG00000185303.14', 'ENSG00000135605.11', 'ENSG00000196260.3', 'ENSG00000151365.2']) #the array containing the mutated GenomicIdentifiers should be passed to this function
