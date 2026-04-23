class Feedback:
    QUESTIONS = [
        "1. How clean and well-organized was the store?",
        "2. How satisfied were you with the customer service?",
        "3. How likely are you to recommend us to a friend?"
    ]
    def __init__(self, org_id: int, mood: str, answers: list):
        self.org_id = org_id
        self.mood = mood
        self.answers = answers