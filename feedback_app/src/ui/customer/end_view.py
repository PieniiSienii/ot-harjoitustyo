from tkinter import ttk, constants


class EndView:
    """Luokka, joka vastaa loppunäkymästä, kun arvostelu on annettu. """

    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        ttk.Frame(self._frame, height=250).pack()

        label = ttk.Label(master=self._frame,
                          text="Thank you for your feedback!",
                          font=("Arial", 12, "bold")
                          )
        label.pack(pady=10)

        close_button = ttk.Button(
            master=self._frame,
            text="Close window",
            command=self._root.destroy
        )
        close_button.pack(pady=10)
