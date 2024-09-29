/*This SQL query is used to create two tables, authors and books. It only creates the columns for the
table which is the features or attributes of the entity to be added.*/

--The next two lines of code will ensure that the tables are not create if they exist.
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

--Create authors table. The authors is create first because it is independent of other tables in database.
CREATE TABLE authors(
    author_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    year_born INTEGER
);

--Create books table.The authors is create second because it is dependent on the author table in database.
CREATE TABLE books(
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY(author_id) REFERENCES authors(author_id)
);