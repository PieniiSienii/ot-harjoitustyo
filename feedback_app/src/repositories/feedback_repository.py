import json
from entities.feedback import Feedback

class FeedbackRepository:
    def __init__(self, file="feedback.json"):
        self._file = file

    def save(self, feedback: Feedback):
        data = self.get_all()
        data.append({"mood": feedback._mood}) # pylint: disable=W0212

        with open(self._file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def get_all(self):
        try:
            with open(self._file, encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
