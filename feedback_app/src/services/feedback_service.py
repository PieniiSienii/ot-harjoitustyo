from entities.feedback import Feedback


class FeedbackService:

    def __init__(self, repository):
        self._repo = repository

    def save_feedback(self, org_id, mood, answers):
        fb = Feedback(org_id, mood, answers)
        self._repo.add_fb(fb)

    def get_all(self):
        return self._repo.get_all()

    def get_average_ratings(self, org_id):
        feedbacks = [fb for fb in self._repo.get_all() if fb.org_id == org_id]
        if not feedbacks:
            return []

        answer_keys = ["Cleanliness", "Customer Service", "Would Recommend"]
        total = {key: 0 for key in answer_keys}

        for fb in feedbacks:
            for i, value in enumerate(fb.answers):
                key = answer_keys[i]
                total[key] += value
        
        return {key: total[key] / len(feedbacks) for key in total}
