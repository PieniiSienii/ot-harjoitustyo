import unittest
from entities.feedback import Feedback


class TestFeedback(unittest.TestCase):
    def setUp(self):
        self.feedback = Feedback(1, "ok", [5, 5, 5])

    def test_feedback_info_is_set_correct(self):
        self.assertEqual(self.feedback.mood, "ok")
        self.assertEqual(self.feedback.answers, [5, 5, 5])
        self.assertEqual(self.feedback.org_id, 1)
