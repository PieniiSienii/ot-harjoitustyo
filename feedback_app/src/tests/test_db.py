import sqlite3


def get_test_db_connection():
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    create_test_tables(connection)
    return connection


def create_test_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
                CREATE TABLE feedback (
                   id INTEGER PRIMARY KEY,
                   org_id INTEGER,
                   mood TEXT,
                   answers TEXT
            )""")

    cursor.execute("""
                CREATE TABLE organizations (
                   id INTEGER PRIMARY KEY,
                   name TEXT)
                """)

    connection.commit()
