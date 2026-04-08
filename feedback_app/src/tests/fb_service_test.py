import unittest
from unittest.mock import patch
from services.feedback_service import FeedbackService
from entities.feedback import Feedback

class FakeRepoForTest:
    def __init__(self):
        self.saved = []
    
    def save(self, fb):
        self.saved.append(fb)
    
    def get_all(self):
        return self.saved

class TestFeedbackService(unittest.TestCase):
    @patch("builtins.input", return_value="good")
    def test_fb_saves_correctly(self, input):
        repo = FakeRepoForTest()
        service = FeedbackService(repo)
        service.ask_feedback()

        self.assertEqual(len(repo.saved), 1)
        self.assertEqual(repo.saved[0]._mood, "good")