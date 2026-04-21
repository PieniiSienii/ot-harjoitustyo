from db_connection import get_db_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS feedback")
    cursor.execute("DROP TABLE IF EXISTS organizations")

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
                CREATE TABLE feedback (
                   id INTEGER PRIMARY KEY,
                   org_id INTEGER,
                   mood TEXT,
                   rating INTEGER,
                   question1 INTEGER,
                   question2 INTEGER
            )""")

    cursor.execute("""
                CREATE TABLE organizations (
                   id INTEGER PRIMARY KEY,
                   name TEXT)
                """)

    connection.commit()

def seed_organizations(connection):
    cursor = connection.cursor()

    cursor.execute("INSERT INTO organizations (id, name) VALUES (1, 'Apple')")
    cursor.execute("INSERT INTO organizations (id, name) VALUES (2, 'Power')")
    cursor.execute("INSERT INTO organizations (id, name) VALUES (3, 'Zara')")
    cursor.execute("INSERT INTO organizations (id, name) VALUES (4, 'Prisma')")

    connection.commit()

def initialize_db():
    connection = get_db_connection()
    drop_tables(connection)
    create_tables(connection)
    seed_organizations(connection)

if __name__ == "__main__":
    initialize_db()