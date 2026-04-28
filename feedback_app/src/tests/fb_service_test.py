import unittest
from services.feedback_service import FeedbackService


class FakeRepoForTest:
    def __init__(self):
        self.saved = []

    def add_fb(self, fb):
        self.saved.append(fb)

    def get_all(self):
        return self.saved


class TestFeedbackService(unittest.TestCase):
    def test_fb_saves_correctly(self):
        repo = FakeRepoForTest()
        self.service = FeedbackService(repo)
        self.service.save_feedback(1, "Excellent", [1, 2, 3])

        self.assertEqual(len(repo.saved), 1)
        self.assertEqual(repo.saved[0].mood, "Excellent")
        self.assertEqual(repo.saved[0].answers, [1, 2, 3])
        self.assertEqual(repo.saved[0].org_id, 1)

    def test_get_all_is_correct(self):
        repo = FakeRepoForTest()
        self.service = FeedbackService(repo)
        self.service.save_feedback(1, "Excellent", [2, 2, 2])

        result = self.service.get_all()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].mood, "Excellent")
        self.assertEqual(result[0].answers, [2, 2, 2])

    def test_ratings_are_correct(self):
        repo = FakeRepoForTest()
        self.service = FeedbackService(repo)
        self.service.save_feedback(1, "Excellent", [2, 2, 2])
        self.service.save_feedback(1, "Ok", [4, 4, 4])

        result = self.service.get_average_ratings(1)

        self.assertEqual(result["Cleanliness"], 3.0)
        self.assertEqual(result["Customer Service"], 3.0)
        self.assertEqual(result["Would Recommend"], 3.0)

    def test_correct_average_ratings_by_mood(self):
        repo = FakeRepoForTest()
        self.service = FeedbackService(repo)
        self.service.save_feedback(1, "Excellent", [2, 2, 2])
        self.service.save_feedback(1, "Ok", [4, 4, 4])
        self.service.save_feedback(1, "Excellent", [4, 4, 4])
        result = self.service.get_average_ratings_by_mood(1)
        self.assertEqual(
            result,
            {"Excellent": {"Cleanliness": 3.0, "Customer Service": 3.0, "Would Recommend": 3.0},
             "Ok": {"Cleanliness": 4.0, "Customer Service": 4.0, "Would Recommend": 4.0}
             }
        )
    
    def test_no_feedbacks_returns_empty_dict(self):
        repo = FakeRepoForTest()
        self.service = FeedbackService(repo)
        result_for_avg = self.service.get_average_ratings(1)

        self.assertEqual(result_for_avg, {})

        result_for_avg_by_mood = self.service.get_average_ratings_by_mood(1)
        self.assertEqual(result_for_avg_by_mood, {})