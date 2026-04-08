from entities.feedback import Feedback

class FeedbackService:
    def __init__(self, repository):
        self._repo = repository
    
    def ask_feedback(self):
        self._mood = input("How was your visit today? (bad/ok/good): ") 
        self._fb = Feedback(self._mood)
        self._repo.save(self._fb)
        print("Thank you for your feedback!")