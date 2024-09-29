# datafun-05-sql

Datafun-05-sql combines Python and SQL, emphasizing database interactions through SQLite. This project introduces logging, an essential tool for debugging and monitoring, and involves creating and managing a database, designing a schema, and executing various SQL operations, including queries with joins, filters, and aggregations.

## Process

1. Create a GitHub repository for datafun-05-sql.
2. Clone the repository onto a local machine.
```git clone https://github.com/kwameape123/datafun-05-sql```
3. Create project virtual environment.
```py -m venv .venv```
4. Create project .gitignore file to indicate folders and files to exclude from tracking.
```ni .gitignore```
5. Git pull GitHub repository to ensure project is in sync with that on local machine.
```git pull```
6. Activate virtual environment.
```.venv\Scripts\Activate```
7. Pip install needed python dependencies(pandas and pyarrow) for our project.
```py -m pip install -r requirements.txt```
8. Create the needed files and folders using folder_script.py. Note that the contents of the csv was added using copy and paste.
9. Create database using the create_database function within the database_creator.py script.
10. Create database tables using the create_table function within the database_creator.py script. This function makes use of the books.sql script.
11. Insert data into tables using the insert_record function within the database_creator.py script. This function makes use of the insert_records.sql script.
12. Query our database using the database_query.py script. Note that database_query makes use of the SQL scripts below;
        -delete_records.sql
        -query_aggregation.sql
        -query_filter.sql
        -query_group.sql
        -query_join.sql
        -query_sorting.sql
        -update_records.sql

## Logging

The following log files keeps track of the running of our various python script.
        -log_database_creator.txt
        -log_database_query.txt
        log_folder_script.txt

## Notes

Every script includes comments explaining the above listed process in details. Therefore, refer to the
scripts for more information.


At regular intervals, ensure that the project repository on your local machine is synced with GitHub.
```git add .```
```git commit -m "message"```
```git push origin main```