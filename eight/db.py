import psycopg2
import sqlite3


class Db(object):

    __instance = None
    conn = None

    def __new__(cls):
        if Db.__instance is None:
            Db.__instance = object.__new__(cls)
        return Db.__instance

    def connect(self, dbname, username, password, is_postgres=False, host="127.0.0.1", port=5432):
        if is_postgres:
            try:
                self.conn = psycopg2.connect(dbname=dbname, user=username, password=password, host=host, port=port)
            except psycopg2.OperationalError:
                raise Exception("Connection failed")

        else:
            self.conn = sqlite3.connect(dbname)

        if isinstance(self.conn, sqlite3.Connection):
            print("Connection OK to sqlite3")
        elif isinstance(self.conn, psycopg2.extensions.connection):
            print("Connection OK to PostgreSQL")
        else:
            raise Exception("Connection failed")
