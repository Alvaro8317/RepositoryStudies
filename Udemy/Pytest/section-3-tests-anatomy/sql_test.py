import sqlite3
import unittest

sql = """
CREATE TABLE PERSONAS(
  NAME TEXT,
  LASTNAME TEXT,
  DNI INT4EGER UNIQUE
);
"""


class TestSQL(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.db = sqlite3.connect("test.db")
        self.cursor = self.db.cursor()
        self.cursor.execute(sql)  # Limpia la tabla antes del test
        self.db.commit()

    def test_create_person(self):
        # section -> Creating a person (ACT)
        self.cursor.execute(
            "INSERT INTO PERSONAS (NAME, LASTNAME, DNI) VALUES (?, ?, ?)", ("Alvaro", "Garzón", 123)
        )
        self.db.commit()
        person = self.cursor.execute("SELECT * FROM PERSONAS WHERE PERSONAS.DNI = 123").fetchone()
        # assert person[0] == "Alvaro"
        # assert person[1] == "Garzón"
        # Assert
        assert person[2] == 123
        assert len(person) == 3
        # Tener muchos assert en un test, es mala práctica
        # Clean up
        self.cursor.execute("DELETE FROM PERSONAS WHERE DNI = 123")
        self.db.commit()
        person = self.cursor.execute("SELECT * FROM PERSONAS WHERE PERSONAS.DNI = 123").fetchone()
        assert person is None

    def tearDown(self):
        self.cursor.execute("DROP TABLE PERSONAS")
        self.cursor.close()
        self.db.close()


class TestSQLPytest:
    def test_create_person(self, fxt_database, fxt_cursor, fake_person):
        # section -> Creating a person (ACT)
        fxt_cursor.execute(
            "INSERT INTO PERSONAS (NAME, LASTNAME, DNI) VALUES (?, ?, ?)", fake_person
        )
        fxt_database.commit()
        person = fxt_cursor.execute(f"SELECT * FROM PERSONAS WHERE PERSONAS.DNI = {fake_person[2]}").fetchone()
        # Assert
        assert len(person) == 3
        # Clean up
        fxt_cursor.execute(f"DELETE FROM PERSONAS WHERE DNI = {fake_person[2]}")
        fxt_database.commit()
        person = fxt_cursor.execute(f"SELECT * FROM PERSONAS WHERE PERSONAS.DNI = {fake_person[2]}").fetchone()
        assert person is None
