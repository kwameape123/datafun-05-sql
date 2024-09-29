'''This module is used to create the needed folders
for datafun-05-sql'''

# Import project libraries
import pathlib as pl
import os
import csv
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log_folder_script.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Declare global variables
root_directory = pl.Path.cwd()
data_directory = root_directory.joinpath ('data')
data_directory.mkdir(exist_ok = True)
sql_directory = root_directory.joinpath('sql')
sql_directory.mkdir(exist_ok= True)

def csv_file(filename:str)->None:
    file_path = root_directory/data_directory/filename
    with open(file_path,mode = 'w', newline = '') as file:
        pass

def sql_file(filename:str)->None:
    file_path = root_directory/sql_directory/filename
    with open(file_path,mode = 'w', newline = '') as file:
        pass



def main()->None:
    logging.info("Program Started")
    # csv_file('books.csv')
    # csv_file('authors.csv')
    sql_file('update_records.sql')
    sql_file('delete_records.sql')
    sql_file('query_aggregation.sql')
    sql_file('query_filter.sql')
    sql_file('query_sorting.sql')
    sql_file('query_group.sql')
    sql_file('query_join.sql')
    logging.info("Program, ended")

if __name__ == '__main__':
    main()
