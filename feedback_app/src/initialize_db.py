from db_connection import get_db_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS feedback")
    cursor.execute("DROP TABLE IF EXISTS organizations")
    cursor.execute("DROP TABLE IF EXISTS questions")

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
                CREATE TABLE feedback (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   org_id INTEGER,
                   mood TEXT,
                   answers TEXT
            )""")

    cursor.execute("""
                CREATE TABLE organizations (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT UNIQUE)
                """)

    cursor.execute("""
                CREATE TABLE questions ( 
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   org_id INTEGER,
                   key TEXT,
                   text TEXT
                   )
                """)

    connection.commit()


def seed_questions(connection):
    cursor = connection.cursor()

    questions = {
        "Cleanliness": "1. How clean and well-organized was the store?",
        "Customer Service": "2. How satisfied were you with the customer service?",
        "Would Recommend": "3. How likely are you to recommend us to a friend?"
    }

    for key, q in questions.items():
        cursor.execute(
            "INSERT INTO questions (key, text) VALUES (?,?)",
            (key, q)
        )

    connection.commit()


def seed_organizations(connection):
    cursor = connection.cursor()

    cursor.execute("INSERT INTO organizations (name) VALUES ('Apple')")
    cursor.execute("INSERT INTO organizations (name) VALUES ('Power')")
    cursor.execute("INSERT INTO organizations (name) VALUES ('Zara')")
    cursor.execute("INSERT INTO organizations (name) VALUES ('Prisma')")

    connection.commit()


def initialize_db():
    connection = get_db_connection()
    drop_tables(connection)
    create_tables(connection)
    seed_organizations(connection)
    seed_questions(connection)


if __name__ == "__main__":
    initialize_db()
