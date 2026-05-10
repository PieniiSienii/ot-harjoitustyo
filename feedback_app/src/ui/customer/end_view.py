from tkinter import ttk, constants


class EndView:
    """Class responsible for the final view shown after feedback is submitted."""

    def __init__(self, root):
        """Constructor for the end view."""

        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        """Displays the view."""

        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        """Destroys the view."""

        self._frame.destroy()

    def _initialize(self):
        """Initializes the UI components."""

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
