import sqlite3
import pandas as pd
from src.director import Director

conn = sqlite3.connect('../movie_films_actors.db')
cursor = conn.cursor()

director = Director(id = 5, full_name = 'Francis Ford Coppola')

#root_url = "https://raw.githubusercontent.com/jigsawlabs-student/curriculum-images/main/has-many-movies-lab/"
#names = ['actors', 'directors', 'movies', 'writers', 'movie_actors', 'movie_directors', 'movie_writers']
#loaded_dfs = [pd.read_csv(f'{root_url}{name}.csv') for name in names]

#for index, name in enumerate(names):
#    loaded_dfs[index].to_sql(f'{name}', conn, index = False, if_exists='replace')

#cursor.execute('SELECT name from sqlite_master where type= "table"')
#tables = cursor.fetchall()
#print(tables)
print("")
print("")
print("")
#for table_tuple in tables:
#    table_name = table_tuple[0]
#    print(table_name, 'table')
#    print(pd.read_sql(f'PRAGMA table_info({table_name})', conn)[['name']].T)

#print('Find all attributes of the director who made the movie the martian')
#query = """SELECT d.id, d.name FROM directors d
#            JOIN movie_directors md
#            ON md.director_id = d.id 
#            JOIN movies m
#            ON m.id = md.movie_id
#            WHERE m.title = 'The Martian'"""
#cursor.execute(query)
#results = cursor.fetchone()
#print(pd.read_sql(query, conn).T)
print("")
print("")
print("")

#print('Find the average runtime of Steven Soderbergh movies')
#query = """ SELECT AVG(m.runtime) as avg_runtime FROM movies m
#            JOIN movie_directors md
#            ON m.id = md.movie_id
#            JOIN directors d
#            ON md.director_id = d. id
#            WHERE d.name = 'Steven Soderbergh'"""
#cursor.execute(query)
#results = cursor.fetchall()
#print(results)
print("")
print("")
print("")

print('Find the names and average runtimes of the directors who have made at least three movies and have the top three average runtimes, do not include results that have null values for the average runtime')
query = """ SELECT d.name, AVG(m.runtime) FROM movies m
            JOIN movie_directors md
            ON m.id = md.movie_id
            JOIN directors d
            ON md.director_id = d. id
            GROUP BY d.name
            HAVING count(d.name) >=3
            ORDER by AVG(m.runtime) DESC
            LIMIT 3"""
query = """ SELECT m.id, d.name, AVG(m.runtime), count(*) as amount_movies FROM movies m
            JOIN movie_directors md
            ON m.id = md.movie_id
            JOIN directors d
            ON md.director_id = d. id
            GROUP BY m.id
            HAVING amount_movies >= 3 
            ORDER by AVG(m.runtime) DESC
            LIMIT 3"""
cursor.execute(query)
results = cursor.fetchall()
print(results)
