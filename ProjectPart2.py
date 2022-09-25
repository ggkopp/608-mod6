# coding: utf-8
import sqlite3
connection = sqlite3.connect('books.db')
import pandas as pd
pd.options.display.max_columns = 10
pd.read_sql('SELECT * FROM authors', connection,
            index_col=['id])
pd.read_sql('SELECT * FROM authors', connection,
            index_col=['id'])
pd.read_sql('Select * FROM titles', connection)
pd.read_sql('Select * FROM author_ISBN', connection)
pd.read_sql("""SELECT title, edition, copyright
                FROM titles
                WHERE copyright > '2017""", connection)
pd.read_sql("""SELECT title, edition, copyright
                FROM titles
                WHERE copyright > '2017'""", connection)
pd.read_sql("""SELECT title 
                FROM titles
                WHERE title LIKE '%HOW to%', connection""")
pd.read_sql("""SELECT title FROM titles WHERE title LIKE '%How%'""", connection, index_col['id'])
pd.read_sql("""SELECT title, FROM titles WHERE title LIKE '%How%'""", connection, index_col=['id'])
pd.read_sql("""SELECT title
                FROM titles
                WHERE title LIKE '%How%'""",
                connection, index_col=['id'])
pd.read_sql("""SELECT title, edition
               FROM titles
               WHERE edition > '2'""", connection)     
pd.read_sql("""SELECT id, first, last
                FROM authors
                ORDER BY id, first""",
                connection, index_col=['id'])
pd.read_sql("""SELECT id, first, last
                FROM authors
                ORDER BY id DESC, first ASC""",
                connection, index_col=['id'])
print('Garrett Kopp')
