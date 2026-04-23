from entities.feedback import Feedback


class FeedbackService:

    def __init__(self, repository):
        self._repo = repository

    def save_feedback(self, org_id, mood, answers):
        fb = Feedback(org_id, mood, answers)
        self._repo.add_fb(fb)

    def get_all(self):
        return self._repo.get_all()
