import unittest
from entities.feedback import Feedback

class TestFeedback(unittest.TestCase):
    def setUp(self):
        self.feedback = Feedback("ok")
    def test_mood_is_set_correct(self):
        self.assertEqual(self.feedback._mood, "ok" )