import sqlite3
import pandas as pd

conn = sqlite3.connect('movie_films_actors.db')
cursor = conn.cursor()


root_url = "https://raw.githubusercontent.com/jigsawlabs-student/curriculum-images/main/has-many-movies-lab/"
names = ['actors', 'directors', 'movies', 'writers', 'movie_actors', 'movie_directors', 'movie_writers']
loaded_dfs = [pd.read_csv(f'{root_url}{name}.csv') for name in names]

for index, name in enumerate(names):
    loaded_dfs[index].to_sql(f'{name}', conn, index = False, if_exists='replace')

cursor.execute('SELECT name from sqlite_master where type= "table"')
tables = cursor.fetchall()
print(tables)
print("")
print("")
print("")
for table_tuple in tables:
    table_name = table_tuple[0]
    print(table_name, 'table')
    print(pd.read_sql(f'PRAGMA table_info({table_name})', conn)[['name']].T)
