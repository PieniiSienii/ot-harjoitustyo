from tkinter import ttk, constants


class MoodView:
    def __init__(self, root, handle_mood):
        self._root = root
        self._handle_mood = handle_mood
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text="How was your visit? (ok/good/bad)")

        ok_button = ttk.Button(
            master=self._frame,
            text="ok",
            command=lambda: self._handle_mood("Ok")
        )

        good_button = ttk.Button(
            master=self._frame,
            text="Good",
            command=lambda: self._handle_mood("Good")
        )

        bad_button = ttk.Button(
            master=self._frame,
            text="Bad",
            command=lambda: self._handle_mood("Bad")
        )

        label.grid(row=0, column=0)
        ok_button.grid(row=1, column=0)
        good_button.grid(row=1, column=1)
        bad_button.grid(row=1, column=2)
