import hashlib
import sqlite3


class Database:
    def __init__(self):
        self.connect = None
        self.connection = sqlite3.connect("workout.db")

    def create_table(self, table):
        with self.connection:
            self.connect = self.connection.cursor()
            self.connect.execute(f"""CREATE TABLE IF NOT EXISTS {table} (
                                    name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username varchar(15) NOT NULL,
                                    password varchar(255) NOT NULL
                                 )""")

    def insert_user_into_table(self, table, user):
        with self.connection:
            self.connect = self.connection.cursor()
            self.connect.execute(f"INSERT INTO {table}(username, password) VALUES (:username, :password)",
                                 {"username": user.name, "password": hashlib.md5(user.password.encode()).hexdigest()})

    def get_data_from_table(self, table):
        with self.connection:
            self.connect = self.connection.cursor()
            for row in self.connect.execute(f"SELECT * FROM {table}"):
                print(row)
