import pytest
import sqlite3
from src.director import Director

@pytest.fixture
def cursor():
    conn = sqlite3.connect('../movie_films_actors.db')
    cursor = conn.cursor()

    yield cursor

@pytest.fixture
def director():
    director = Director(
        id = 5, full_name = 'Francis Ford Coppola')

    yield director

def test_is_director_class(director):
    director = Director()
    assert type(director) == Director

def test_directors_first_name(director):
    assert 'Francis' == director.first_name()

def test_directors_last_name(director):
    assert 'Coppola' == director.last_name()

def test_directors_movies(cursor):
    director = Director(
        id = 5, full_name = 'Francis Ford Coppola')
    assert (5, 'Apocalypse Now', 1979) in director.movies(cursor)
