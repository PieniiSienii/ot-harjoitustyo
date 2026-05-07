class Feedback:
    def __init__(self, org_id: int, mood: str, answers: list):
        self.org_id = org_id
        self.mood = mood
        self.answers = answers
