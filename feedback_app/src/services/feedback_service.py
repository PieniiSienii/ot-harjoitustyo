from entities.feedback import Feedback


class FeedbackService:

    def __init__(self, repository):
        self._repo = repository

    def save_feedback(self, org_id, mood, rating):
        fb = Feedback(org_id, mood, rating)
        self._repo.save(fb)

    def get_all(self):
        return self._repo.get_all()
