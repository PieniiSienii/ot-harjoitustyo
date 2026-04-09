from repositories.feedback_repository import FeedbackRepository
from services.feedback_service import FeedbackService

def main():
    repo = FeedbackRepository()
    service = FeedbackService(repo)

    service.ask_feedback()

if __name__ == "__main__":
    main()
