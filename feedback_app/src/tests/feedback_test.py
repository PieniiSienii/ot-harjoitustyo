import unittest
from entities.feedback import Feedback


class TestFeedback(unittest.TestCase):
    def setUp(self):
        self.feedback = Feedback(1, "ok", 3)

    def test_feedback_info_is_set_correct(self):
        self.assertEqual(self.feedback.mood, "ok")
        self.assertEqual(self.feedback.rating, 3)
        self.assertEqual(self.feedback.org_id, 1)
