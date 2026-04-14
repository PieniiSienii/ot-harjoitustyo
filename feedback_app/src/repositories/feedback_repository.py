import json
from entities.feedback import Feedback


class FeedbackRepository:
    def __init__(self, file="feedback.json"):
        self._file = file

    def save(self, feedback: Feedback):
        data = self.get_all()
        data.append({"org_id": feedback.org_id,
                    "mood": feedback.mood,
                     "rating": feedback.rating})

        with open(self._file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def get_all(self):
        try:
            with open(self._file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
