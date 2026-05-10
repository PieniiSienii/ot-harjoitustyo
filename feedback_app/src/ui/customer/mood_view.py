from tkinter import ttk, constants


class MoodView:
    """ Luokka, joka vastaa päivän fiilis kysymyksen näyttämisestä"""

    def __init__(self, root, handle_mood, go_back):
        self._root = root
        self._handle_mood = handle_mood
        self._frame = None
        self._go_back = go_back

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
            text="How is your overall mood today?",
            font=("Arial", 14, "bold"))

        label.pack(pady=10)

        button_frame = ttk.Frame(self._frame)
        button_frame.pack(pady=10)

        excellent_button = ttk.Button(
            master=button_frame,
            text="Excellent",
            command=lambda: self._handle_mood("Excellent")
        )

        ok_button = ttk.Button(
            master=button_frame,
            text="Ok",
            command=lambda: self._handle_mood("Ok")
        )

        bad_button = ttk.Button(
            master=button_frame,
            text="Bad",
            command=lambda: self._handle_mood("Bad")
        )

        excellent_button.pack(side="left", padx=5)
        ok_button.pack(side="left", padx=5)
        bad_button.pack(side="left", padx=5)

        ttk.Button(
            master=self._frame,
            text="Back",
            command=self._go_back
        ).pack(pady=15)
