from entities.feedback import Feedback


class FeedbackService:

    def __init__(self, repository):
        self._repo = repository

    def save_feedback(self, org_id, mood, rating, q1=None, q2=None):
        fb = Feedback(org_id, mood, rating, q1, q2)
        self._repo.add_fb(fb)

    def get_all(self):
        return self._repo.get_all()
