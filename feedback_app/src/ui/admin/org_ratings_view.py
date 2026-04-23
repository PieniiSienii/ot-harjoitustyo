from tkinter import ttk, constants


class OrgRatingsView:
    def __init__(self, root, feedbacks, averages, go_back):
        self._root = root
        self._frame = None
        self._feedbacks = feedbacks
        self._averages = averages
        self._go_back = go_back

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X, expand=True)

    def destroy(self):
        self._frame.destroy()

    def hide(self):
        self._frame.pack_forget()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame,
                          text="Organization feedbacks")
        label.grid(row=0, column=0, columnspan=5)
        average_text = ttk.Label(master=self._frame, text= "Averages:")
        row = 2
        answer_keys = ["Cleanliness", "Customer Service", "Would Recommend"]

        if self._averages != []:
            average_text.grid(row=1, column=0, columnspan=5)
            for key in answer_keys:
                text = f"{key} {self._averages[key]}"
                label = ttk.Label(master=self._frame, text=text)
                label.grid(row=row, column=0)
                row += 1
        else:
            ttk.Label(
                master=self._frame,
                text="No ratings yet"
            ).grid(row=1, column=0,columnspan=2)


        ttk.Button(
            master=self._frame,
            text="Back",
            command=self._go_back
        ).grid(row=row, column=0)

        close_button = ttk.Button(
            master=self._frame,
            text="Close window",
            command=self._root.destroy
        )
        close_button.grid(row=6, column=0, pady= 8, columnspan=10)
