from tkinter import ttk, constants


class MoodView:
    def __init__(self, root, handle_mood, go_back):
        self._root = root
        self._handle_mood = handle_mood
        self._frame = None
        self._go_back = go_back

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text="How is your overall mood today? (Excellent/ Ok/ Bad)")

        excellent_button = ttk.Button(
            master=self._frame,
            text="Excellent",
            command=lambda: self._handle_mood("Good")
        )

        ok_button = ttk.Button(
            master=self._frame,
            text="Ok",
            command=lambda: self._handle_mood("Ok")
        )

        bad_button = ttk.Button(
            master=self._frame,
            text="Bad",
            command=lambda: self._handle_mood("Bad")
        )

        ttk.Button(
            master=self._frame,
            text="Back",
            command=self._go_back
        ).grid(row=4, column=0, pady=8)

        label.grid(row=0, column=0, columnspan=2)
        excellent_button.grid(row=1, column=0)
        ok_button.grid(row=1, column=1)
        bad_button.grid(row=1, column=2)
