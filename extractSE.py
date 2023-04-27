"""
Program: CSV data extraction and conversion
Author: Shuijin Li
Email: skli@dundee.ac.uk
Date: 12 Mar 2023

This program reads CSV files from the './output' subdirectory, extracts data based on specific criteria,
and saves the extracted data as text files in the same directory. The program then moves the extracted
text files back to the './output' subdirectory.

The program uses the following libraries:

os: provides access to operating system functionalities such as file handling
pandas: provides data manipulation and analysis tools
"""

import os
import pandas as pd

# Find all .csv files in the 'output' subdirectory
files = [f for f in os.listdir('./output') if f.endswith('.csv')]

# Set the block name and columns to extract from each file
blockName = ' block=1'
variablesToExtract = ['Block Name','Time','avg(Y)']

# Loop over each CSV file
for filename in files:
    filepath = os.path.join('./output', filename)
    data = pd.read_csv(filepath, usecols=variablesToExtract)
    indices = data.iloc[:, 0] == blockName
    dat = data.loc[indices, :]
    dat = dat.drop(variablesToExtract[0], axis=1)

    # Save the extracted data to a .txt file with the same name
    name = os.path.splitext(os.path.basename(filename))[0]
    outfile = os.path.join('./output', f'{name}.txt')
    dat = dat[['Time','avg(Y)']]
    dat.to_csv(outfile, sep=' ', index=False, header=False)

    # Print a message to confirm successful execution
    print(f'Data extracted and saved to {outfile}.')


# Move all extracted .txt files to the 'output' subdirectory
for file in os.listdir('./output'):
    if file.endswith('.txt'):
        os.rename(os.path.join('./output', file), os.path.join('./output', file))
