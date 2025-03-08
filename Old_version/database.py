import psycopg2
from psycopg2 import OperationalError, sql


class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.ensure_database()

    def ensure_database(self):
        try:
            # Connect to the default database to check for and create the target database
            default_connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database="postgres"
            )
            default_connection.autocommit = True

            with default_connection.cursor() as cursor:
                cursor.execute(sql.SQL(
                    "SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"
                ), [self.database])

                exists = cursor.fetchone()
                if not exists:
                    cursor.execute(sql.SQL(
                        "CREATE DATABASE {}"
                    ).format(sql.Identifier(self.database)))
                    print(f"Database {self.database} created successfully")

            default_connection.close()

            # Connect to the target database
            self.connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print(f"Connected to database {self.database} successfully")

        except OperationalError as e:
            print(f"Error ensuring database: {e}")
            raise e

    def execute_query(self, query, params=None, fetch=False):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if fetch:
                return cursor.fetchall()
            else:
                self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
