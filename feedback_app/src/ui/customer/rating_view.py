from tkinter import ttk, constants


class RatingView:
    def __init__(self, root, handle_rating):
        self._root = root
        self._handle_rating = handle_rating
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Rate your visit (1-5)")

        for num in range(1, 6):
            ttk.Button(
                self._frame,
                text=str(num),
                command=lambda r=num: self._handle_rating(r)
            ).grid(row=1, column=(num))

        label.grid(row=0, column=0, columnspan=5)
