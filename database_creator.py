# Import needed module or libraries
import pandas as pd
import sqlite3
import pathlib

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

def main():
    create_database()
    create_table()

if __name__ == "__main__":
    main()
