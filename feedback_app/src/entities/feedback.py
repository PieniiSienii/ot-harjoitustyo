class Feedback:
    """Class representing a single customer feedback entry.
    Attributes:
        org_id: ID of the organization the feedback belongs to.
        mood: Customer's day mood (Excellent, Ok, Bad)
        answers: List or numeric answers to feedback questions.
    """
    def __init__(self, org_id: int, mood: str, answers: list):
        """Constructor for creating a new feedback entry.

        Args:
            org_id (int): ID of the organization.
            mood (str): Customer mood
            answers (list): List of answers
        """
        self.org_id = org_id
        self.mood = mood
        self.answers = answers
