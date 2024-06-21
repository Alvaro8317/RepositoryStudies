import sqlite3

db = sqlite3.connect("test.db")
sql = """
CREATE TABLE PERSONAS(
  NAME TEXT,
  LASTNAME TEXT,
  DNI INTEGER UNIQUE
);
"""
cursor = db.cursor()
cursor.execute(sql)