import psycopg2
from pprint import pprint

class DatabaseConnection:
    def _init_(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='testpython' user='adammorris' host='localhost' password='summer22' port='5432' ")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Cannot connect to database")
    def create_table(self):
        create_table_command = "CREATE TABLE pet(id serial PRIMARY KEY, name varchar(100), age integer NOT NULL)"
        self.cursor.execute(create_table_command)

if __name__ == "__main__":
    database_connection = DatabaseConnection()
    database_connection.create_table()
