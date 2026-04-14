import unittest
from unittest import mock
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
    def test_fb_saves_correctly(self):
        repo = FakeRepoForTest()
        service = FeedbackService(repo)
        service.save_feedback(1, "good", 4)

        self.assertEqual(len(repo.saved), 1)
        self.assertEqual(repo.saved[0].mood, "good")
        self.assertEqual(repo.saved[0].rating, 4)
        self.assertEqual(repo.saved[0].org_id, 1)
