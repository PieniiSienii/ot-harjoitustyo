import unittest
from entities.feedback import Feedback


class TestFeedback(unittest.TestCase):
    def setUp(self):
        self.feedback = Feedback("ok", 3)

    def test_mood_is_set_correct(self):
        self.assertEqual(self.feedback.mood, "ok")
        self.assertEqual(self.feedback.rating, 3)
