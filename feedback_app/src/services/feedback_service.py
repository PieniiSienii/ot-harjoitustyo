from entities.feedback import Feedback


class FeedbackService:
    """Class responsible for feedback-related logic."""

    def __init__(self, repository, question_repository):
        """Constructor for the feedback service.

        Args:
            repository: Repository used for feedback storage 
            question_repository: Repository used for fetching questions
        """
        self._repo = repository
        self._question_repo = question_repository

    def save_feedback(self, org_id, mood, answers):
        """Saves a new feedback entry.

        Args:
            org_id: ID of the target organization.
            mood: Customer's overall mood
            answers: List of answers on a 1-5 scale
        """

        fb = Feedback(org_id, mood, answers)
        self._repo.add_fb(fb)

    def get_all(self):
        """Returns all saved feedback"""
        return self._repo.get_all()

    def get_average_ratings(self, org_id):
        """Calculates average ratings for each question

        Args:
            org_id: ID of the organization

        Returns:
            Dictionary where keys are question categories
            and values are average ratings.
        """
        feedbacks = [fb for fb in self._repo.get_all() if fb.org_id == org_id]
        if not feedbacks:
            return {}

        answer_keys = [q["key"] for q in self.get_questions()]
        total = {key: 0 for key in answer_keys}

        for fb in feedbacks:
            for i, value in enumerate(fb.answers):
                key = answer_keys[i]
                total[key] += value

        return {key: total[key] / len(feedbacks) for key in total}

    def get_average_ratings_by_mood(self, org_id):
        """Calculates average ratings grouped by mood

        Args:
            org_id: ID of the organization.

        Returns:
            Dictionary where moods map to dictionaries
            containing question averages.
        """
        feedbacks = [fb for fb in self._repo.get_all() if fb.org_id == org_id]

        if not feedbacks:
            return {}

        mood_grouped_ratings = self._group_by_mood(feedbacks)
        return self._calc_averages(mood_grouped_ratings)

    def _group_by_mood(self, feedbacks):
        """Groups feedback answers by mood."""
        mood_grouped_ratings = {}

        for fb in feedbacks:
            if fb.mood not in mood_grouped_ratings:
                mood_grouped_ratings[fb.mood] = []

            mood_grouped_ratings[fb.mood].append(fb.answers)

        return mood_grouped_ratings

    def _calc_averages(self, mood_grouped_ratings):
        """Calculates averages from grouped by mood."""
        answer_keys = [q["key"] for q in self.get_questions()]

        result = {}

        for mood, answer_list in mood_grouped_ratings.items():
            totals = [0] * len(answer_keys)

            for answers in answer_list:
                for i in range(len(answer_keys)):
                    totals[i] += answers[i]

            count = len(answer_list)

            result[mood] = {
                key: totals[i] / count
                for i, key in enumerate(answer_keys)
            }
        return result

    def get_questions(self):
        """Fetches all feedback questions."""
        return self._question_repo.get_all()

    def calc_overall_rating(self, org_id):
        """Calculates the overall average rating."""
        total = 0
        feedbacks = [fb for fb in self._repo.get_all() if fb.org_id == org_id]

        if not feedbacks:
            return {}

        count = len(self.get_questions()) * len(feedbacks)

        for fb in feedbacks:
            total += sum(fb.answers)

        return total / count

    def get_rating_status(self, org_id):
        """Retruns a status label based on overall rating."""
        rating = self.calc_overall_rating(org_id)
        if rating == {}:
            return None

        if rating >= 4.5:
            return "Excellent"

        if rating >= 3.5:
            return "Good"

        if rating >= 2.5:
            return "Ok"

        return "Poor"

    def get_mood_differences(self, org_id):
        """Calculates rating differences between Excellent and Bad moods."""
        averages_by_mood = self.get_average_ratings_by_mood(org_id)
        result = {}

        if "Excellent" not in averages_by_mood or "Bad" not in averages_by_mood:
            return result

        for key in averages_by_mood["Excellent"]:
            difference = (
                averages_by_mood["Excellent"][key]
                - averages_by_mood["Bad"][key]
            )

            result[key] = round(difference, 2)

        return result
