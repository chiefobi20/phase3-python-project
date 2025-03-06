from models.__init__ import CONN, CURSOR

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT
            )
        """
        CURSOR.execute(sql)