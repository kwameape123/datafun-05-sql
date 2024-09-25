'''This module is used to create the needed folders
for datafun-05-sql'''

# Import project libraries
import pathlib as pl
import os
import csv

# Declare global variables
root_directory = pl.Path.cwd()
data_directory = root_directory.joinpath ('data')
data_directory.mkdir(exist_ok = True)

def csv_file(filename:str)->None:
    file_path = root_directory/data_directory/filename
    with open(file_path,mode = 'w', newline = '') as file:
        pass



def main()->None:
    csv_file('books.csv')
    csv_file('authors.csv')

if __name__ == '__main__':
    main()
