import unittest
import os
import json
from entities.feedback import Feedback
from repositories.feedback_repository import FeedbackRepository

class TestFbRepository(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_fb.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.repo = FeedbackRepository(self.test_file)

    def remove_test_file(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_save_and_load(self):
        fb = Feedback("ok")
        self.repo.save(fb)
        all_data = self.repo.get_all()

        self.assertEqual(len(all_data), 1)
        self.assertEqual(all_data[0]["mood"], "ok")