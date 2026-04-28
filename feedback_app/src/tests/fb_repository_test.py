import unittest
from tests.test_db import get_test_db_connection
from entities.feedback import Feedback
from repositories.feedback_repository import FeedbackRepository


class TestFbRepository(unittest.TestCase):
    def setUp(self):
        self.connection = get_test_db_connection()
        self.repo = FeedbackRepository(self.connection)

    def test_save_and_load(self):
        fb = Feedback(1, "ok", [1, 2, 3])

        self.repo.add_fb(fb)
        all_data = self.repo.get_all()

        self.assertEqual(len(all_data), 1)
        self.assertEqual(all_data[0].mood, "ok")
        self.assertEqual(all_data[0].answers, [1, 2, 3])
        self.assertEqual(all_data[0].org_id, 1)
