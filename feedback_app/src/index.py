from tkinter import Tk
from repositories.feedback_repository import FeedbackRepository
from repositories.organizations_repository import OrganizationRepository
from repositories.questions_repository import QuestionsRepository
from services.feedback_service import FeedbackService
from db_connection import get_db_connection
from ui.ui import UI


def main():
    window = Tk()
    window.geometry("600x400")
    window.title("Feedback App")
    connection = get_db_connection()
    q_repo = QuestionsRepository(connection)
    repo = FeedbackRepository(connection)
    service = FeedbackService(repo, q_repo)
    org_repo = OrganizationRepository(connection)
    ui = UI(window, service, org_repo)
    ui.start()
    window.mainloop()

if __name__ == "__main__":
    main()
