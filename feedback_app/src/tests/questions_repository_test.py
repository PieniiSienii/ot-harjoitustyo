import unittest
from tests.test_db import get_test_db_connection
from repositories.questions_repository import QuestionsRepository


class TestQuestionRepository(unittest.TestCase):
    def setUp(self):
        self.connection = get_test_db_connection()
        self.repo = QuestionsRepository(self.connection)

    def test_save_and_load(self):
        cursor = self.connection.cursor()

        cursor.execute("""
                    INSERT INTO questions (
                    id, org_id, key, text)
                    VALUES (?, ?, ?, ?)
                    """,
                       (1, 1, "Cleanliness", "q1"),
                       )

        cursor.execute("""
                    INSERT INTO questions (
                    id, org_id, key, text)
                    VALUES (?, ?, ?, ?)
                    """,
                       (2, 1, "Customer Service", "q2"),
                       )

        cursor.execute("""
                    INSERT INTO questions (
                    id, org_id, key, text)
                    VALUES (?, ?, ?, ?)
                    """,
                       (3, 1, "Would Recommend", "q3"),
                       )

        self.connection.commit()

        all = self.repo.get_all()

        self.assertEqual(len(all), 3)
        self.assertEqual(all[0], {"key": "Cleanliness", "text": "q1"})
        self.assertEqual(all[1], {"key": "Customer Service", "text": "q2"})
        self.assertEqual(all[2], {"key": "Would Recommend", "text": "q3"})
