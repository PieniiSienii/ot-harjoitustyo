import json
from entities.feedback import Feedback


class FeedbackRepository:
    """Repository class responsible for feedback database operations."""

    def __init__(self, connection):
        """Constructor for the feedback repository
        
        Args:
            connection: SQLite database connection object.
        """
        self._connection = connection

    def add_fb(self, feedback: Feedback):
        """Saves a feedback entry to the question.
        Args:
            feedback: Feedback object to be stored.
        """
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
        """Fetches all feedback entries from the database.

        Returns:
            List of Feedback objects
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM feedback")
        rows = cursor.fetchall()

        return [Feedback(
            row["org_id"],
            row["mood"],
            json.loads(row["answers"]))
            for row in rows]
