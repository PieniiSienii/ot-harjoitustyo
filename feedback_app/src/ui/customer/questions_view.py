from tkinter import ttk, constants
from entities.feedback import Feedback


class QuestionsView:
    def __init__(self, root, handle_questions, go_back):
        self._root = root
        self._handle_questions = handle_questions
        self._frame = None
        self._go_back = go_back
        self._answers = []
        self._curr_question = 0

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text="Answer the questions (1-5)")

        self._question_label = ttk.Label(
            master=self._frame,
            text=Feedback.QUESTIONS[self._curr_question]
        )

        for num in range(1, 6):
            ttk.Button(
                self._frame,
                text=str(num),
                command=lambda r=num: self._handle_rating(r)
            ).grid(row=2, column=(num))

        ttk.Button(
            master=self._frame,
            text="Back",
            command=self._go_back
        ).grid(row=4, column=0, pady=8)

        label.grid(row=0, column=0, columnspan=5)
        self._question_label.grid(row=1, column=0, columnspan=5)

    def _handle_rating(self, rating):
        self._answers.append(rating)
        self._curr_question += 1

        if self._curr_question < len(Feedback.QUESTIONS):
            self._question_label.config(
                text=Feedback.QUESTIONS[self._curr_question])

        else:
            self._handle_questions(self._answers)
