import unittest
from services.feedback_service import FeedbackService


class FakeQUestionRepoForTest:
    def __init__(self):
        self._questions = [
            {"key": "Cleanliness", "text": "1. How clean and well-organized was the store?"},
            {"key": "Customer Service",
                "text": "2. How satisfied were you with the customer service?"},
            {"key": "Would Recommend",
                "text": "3. How likely are you to recommend us to a friend?"}
        ]

    def get_all(self):
        return self._questions


class FakeRepoForTest:
    def __init__(self):
        self.saved = []

    def add_fb(self, fb):
        self.saved.append(fb)

    def get_all(self):
        return self.saved


class TestFeedbackService(unittest.TestCase):
    def setUp(self):
        self.q_repo = FakeQUestionRepoForTest()
        self.repo = FakeRepoForTest()
        self.service = FeedbackService(self.repo, self.q_repo)

    def test_fb_saves_correctly(self):
        self.service.save_feedback(1, "Excellent", [1, 2, 3])

        self.assertEqual(len(self.repo.saved), 1)
        self.assertEqual(self.repo.saved[0].mood, "Excellent")
        self.assertEqual(self.repo.saved[0].answers, [1, 2, 3])
        self.assertEqual(self.repo.saved[0].org_id, 1)

    def test_get_all_is_correct(self):
        self.service.save_feedback(1, "Excellent", [2, 2, 2])

        result = self.service.get_all()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].mood, "Excellent")
        self.assertEqual(result[0].answers, [2, 2, 2])

    def test_ratings_are_correct(self):
        self.service.save_feedback(1, "Excellent", [2, 2, 2])
        self.service.save_feedback(1, "Ok", [4, 4, 4])

        result = self.service.get_average_ratings(1)

        self.assertEqual(result["Cleanliness"], 3.0)
        self.assertEqual(result["Customer Service"], 3.0)
        self.assertEqual(result["Would Recommend"], 3.0)

    def test_correct_average_ratings_by_mood(self):
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

    def test_get_average_ratings_by_mood_no_feedbacks_returns_empty_dict(self):
        result_for_avg = self.service.get_average_ratings(1)

        self.assertEqual(result_for_avg, {})

        result_for_avg_by_mood = self.service.get_average_ratings_by_mood(1)
        self.assertEqual(result_for_avg_by_mood, {})

    def test_calc_overall_rating_returns_empty_dict(self):
        result_for_overall_rating = self.service.calc_overall_rating(1)
        self.assertEqual(result_for_overall_rating, {})

    def test_calc_overall_rating_returns_right_average(self):
        self.service.save_feedback(1, "Excellent", [2, 2, 2])
        self.service.save_feedback(1, "Ok", [4, 4, 4])
        result = self.service.calc_overall_rating(1)

        self.assertEqual(result, 3.0)

    def test_get_rating_status_excellent(self):
        self.service.save_feedback(1, "Excellent", [5, 5, 5])
        result = self.service.get_rating_status(1)
        self.assertEqual(result, "Excellent")

    def test_get_rating_status_good(self):
        self.service.save_feedback(1, "Ok", [4, 4, 4])
        result = self.service.get_rating_status(1)
        self.assertEqual(result, "Good")

    def test_get_rating_status_ok(self):
        self.service.save_feedback(1, "Excellent", [2, 3, 3])
        result = self.service.get_rating_status(1)
        self.assertEqual(result, "Ok")

    def test_get_rating_status_poor(self):
        self.service.save_feedback(1, "Ok", [1, 2, 1])
        result = self.service.get_rating_status(1)
        self.assertEqual(result, "Poor")

    def test_get_mood_diff_returns_correct(self):
        self.service.save_feedback(1, "Excellent", [5, 5, 5])
        self.service.save_feedback(1, "Bad", [3, 3, 3])
        result = self.service.get_mood_differences(1)

        self.assertEqual(result["Cleanliness"], 2.0)
        self.assertEqual(result["Customer Service"], 2.0)
        self.assertEqual(result["Would Recommend"], 2.0)
    
    def test_get_mood_diff_returns_empty(self):
        self.service.save_feedback(1, "Bad", [5, 5, 5])

        self.assertEqual(self.service.get_mood_differences(1), {})