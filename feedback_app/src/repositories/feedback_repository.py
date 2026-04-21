from entities.feedback import Feedback


class FeedbackRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_fb(self, feedback: Feedback):
        cursor = self._connection.cursor()

        cursor.execute("""
                    INSERT INTO feedback(org_id, mood, rating, question1, question2)
                    VALUES (?, ?, ?, ?, ?)
                    """, (
                        feedback.org_id,
                        feedback.mood,
                        feedback.rating,
                        feedback.q1,
                        feedback.q2
                    ))
        self._connection.commit()

    def get_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM feedback")
        rows = cursor.fetchall()

        return [Feedback(
            row["org_id"],
            row["mood"],
            row["rating"],
            row["q1"],
            row["q2"])
            for row in rows]