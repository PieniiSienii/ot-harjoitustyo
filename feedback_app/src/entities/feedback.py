class Feedback:
    def __init__(self, org_id: int, mood: str, rating: int, q1: int, q2: int):
        self.org_id = org_id
        self.mood = mood
        self.rating = rating
        self.q1 = q1
        self.q2 = q2
