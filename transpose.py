import pandas as pd
from pathlib import Path

filePath = Path(input("Enter the file path of the csv file:"))

outputFile = input("Enter the name of the output file:")

df = pd.read_csv(filePath)
print(df[:5])
df.set_index('GenomicIdentifier', inplace = True)
print(df[:5])
df = df.T

df.to_csv(outputFile)


