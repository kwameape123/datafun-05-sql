# Import needed module or libraries
import pandas as pd # External module
import sqlite3
import pathlib
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log_database_creator.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Create a file path for the database
db_file = pathlib.Path('books.db')

# Create our books database
def create_database():
    try:
        connection = sqlite3.connect(db_file)
        connection.close()
        print('Books database created successfully')
    except sqlite3.Error as e:
        print(f"Database creation Error: {e}")

# Create our database tables using book.sql script
def create_table():
    try:
        with sqlite3.connect(db_file) as connection:
            sql_file = pathlib.Path('sql', 'books.sql')
            with open(sql_file, 'r') as file:
                sql_scripts = file.read()  # Add parentheses to call the read method
                connection.executescript(sql_scripts)
                print('Tables are good to go')
    except sqlite3.Error as e:
        print(f'Table creation Error: {e}')

# Insert records or data into our tables using the insert_records.sql script
def insert_record():
    try:
        with sqlite3.connect(db_file) as connection:
            sql_file = pathlib.Path('sql', 'insert_records.sql')
            with open(sql_file, 'r') as file:
                sql_scripts = file.read()  # Add parentheses to call the read method
                connection.executescript(sql_scripts)
                print('records has been inserted')
    except sqlite3.Error as e:
        print(f'Records insertion Error: {e}')

#Define our main function to execute our python script as a standalone script.
def main():
    logging.info("Program started")
    #create_database()
    #create_table()
    #insert_record()
    logging.info("Program ended")

if __name__ == "__main__":
    main()
