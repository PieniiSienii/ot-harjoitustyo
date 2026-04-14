from tkinter import ttk, constants


class OrgRatingsView:
    def __init__(self, root, feedbacks):
        self._root = root
        self._feedbacks = feedbacks
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame,
                          text="Organization feedbacks")
        row = 1
        for feedback in self._feedbacks:
            text = f"Mood: {feedback["mood"]}, Rating: {feedback["rating"]}"
            label = ttk.Label(master=self._frame, text=text)
            label.grid(row=row, column=0)
            row += 1

        label.grid(row=0, column=0)
