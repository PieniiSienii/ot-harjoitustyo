import json
from entities.feedback import Feedback


class FeedbackRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_fb(self, feedback: Feedback):
        cursor = self._connection.cursor()

        cursor.execute("""
                    INSERT INTO feedback(org_id, mood, answers)
                    VALUES (?, ?, ?)
                    """, (
            feedback.org_id,
            feedback.mood,
            json.dumps(feedback.answers),
        ))
        self._connection.commit()

    def get_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM feedback")
        rows = cursor.fetchall()

        return [Feedback(
            row["org_id"],
            row["mood"],
            json.loads(row["answers"]))
            for row in rows]
