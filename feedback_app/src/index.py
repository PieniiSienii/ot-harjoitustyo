from tkinter import Tk
from repositories.feedback_repository import FeedbackRepository
from services.feedback_service import FeedbackService
from ui.ui import UI


def main():
    window = Tk()
    window.title("Feedback App")
    repo = FeedbackRepository()
    service = FeedbackService(repo)
    ui = UI(window, service)
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    main()
