import sqlite3
import os
import logging
from pathlib import Path

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log_database_query.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Declare needed variables and file paths
current_directory = Path.cwd()
sql_folder = current_directory/'sql'

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_folder/sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

def main():
    logging.info('Program started')
    execute_sql_from_file('books.db','query_aggregation.sql')
    execute_sql_from_file('books.db','query_filter.sql')
    execute_sql_from_file('books.db','query_group.sql')
    execute_sql_from_file('books.db','query_join.sql')
    execute_sql_from_file('books.db','query_sorting.sql')
    execute_sql_from_file('books.db','update_records.sql')
    execute_sql_from_file('books.db','delete_records.sql')
    logging.info('All SQL operations completed successfully')

if __name__ == "__main__":
    main()
