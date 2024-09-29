--Add the year of birth for George Orwell
UPDATE authors
SET year_born = 1982
WHERE last_name = 'Orwell';

--Change author ID.
UPDATE books
SET author_id = '16f3e0a1-24cb-4ed6-a50d-509f63e367f7'
WHERE author_id = '06cf58ab-90f1-448d-8e54-055e4393e75c';