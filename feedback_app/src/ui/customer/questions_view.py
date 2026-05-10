from tkinter import ttk, constants
from entities.feedback import Feedback


class QuestionsView:
    """Class responsible for displaying the feedback questions view."""

    def __init__(self, root, handle_questions, go_back, service):
        """Constructor for the questions view."""

        self._handle_questions = handle_questions
        self._go_back = go_back
        self._service = service

        self._frame = None
        self._answers = []
        self._curr_question = 0

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        ttk.Frame(self._frame, height=80).pack()

        label = ttk.Label(
            master=self._frame,
            text="Answer the questions (1-5)",
            font=("Arial", 14, "bold")
        )
        label.pack(pady=10)

        self._question_label = ttk.Label(
            master=self._frame,
            text=self._service.get_questions()[self._curr_question]["text"],
            font=("Arial", 12),
            wraplength=400,
            justify="center"
        )
        self._question_label.pack(pady=15)

        button_frame = ttk.Frame(self._frame)
        button_frame.pack(pady=10)

        for num in range(1, 6):
            ttk.Button(
                master=button_frame,
                text=str(num),
                command=lambda r=num: self._handle_rating(r)
            ).pack(side="left", padx=5)

        ttk.Button(
            master=self._frame,
            text="Back",
            command=self._go_back
        ).pack(pady=20)

    def _handle_rating(self, rating):
        """Handles saving a rating and moving to the next question.

        Args:
            rating: Integer rating (1-5)
        """

        self._answers.append(rating)
        self._curr_question += 1

        if self._curr_question < len(self._service.get_questions()):
            self._question_label.config(
                text=self._service.get_questions()[self._curr_question]["text"]
            )

        else:
            self._handle_questions(self._answers)
