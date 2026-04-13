from entities.feedback import Feedback


class FeedbackService:

    def __init__(self, repository):
        self._repo = repository

    def save_feedback(self, mood, rating):
        fb = Feedback(mood, rating)
        self._repo.save(fb)
