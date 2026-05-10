class QuestionsRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT key, text FROM questions ORDER BY id")
        return [{"key": row["key"], "text": row["text"]} for row in cursor.fetchall()]
