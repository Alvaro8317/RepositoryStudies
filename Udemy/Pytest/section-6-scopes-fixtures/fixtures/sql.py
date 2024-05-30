import sqlite3
import pytest

sql_creation_table: str = """
CREATE TABLE PERSONAS(
  NAME TEXT,
  LASTNAME TEXT,
  DNI INT4EGER UNIQUE
);
"""


@pytest.fixture()
def fxt_database():
    db = sqlite3.connect("test.db")  # pytest trabaja a nivel de la ruta tests
    yield db
    db.close()


@pytest.fixture()
def fxt_cursor(fxt_database):
    cursor = fxt_database.cursor()
    cursor.execute(sql_creation_table)
    yield cursor
    cursor.execute("DROP TABLE PERSONAS")
    cursor.close()


@pytest.fixture()
def fake_person():
    return "Alvaro", "Garzon", 1234
