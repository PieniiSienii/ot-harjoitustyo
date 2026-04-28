from tkinter import ttk, constants


class OrgRatingsView:
    """Luokka, joka vastaa organisaation arvostelunäkymästä"""

    def __init__(self, root, feedbacks, averages, averages_by_mood, go_back):
        self._root = root
        self._feedbacks = feedbacks
        self._averages = averages
        self._averages_by_mood = averages_by_mood
        self._go_back = go_back
        self._frame = None
        self._mood_frame = None
        self._answer_keys = ["Cleanliness", "Customer Service", "Would Recommend"]


        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame, text="Organization feedbacks")
        label.grid(row=0, column=0, columnspan=5)

        row = 2

        if self._averages:
            ttk.Label(master=self._frame, text="Averages").grid(
                row=row, column=0, columnspan=5, sticky="w")

            for key in self._answer_keys:
                ttk.Label(
                    master=self._frame,
                    text=f"{key} {self._averages[key]}"
                ).grid(row=row, column=0, sticky="w")
                row += 1

            self._toggle_row = row
            ratings_by_moood_button = ttk.Button(
                master=self._frame,
                text="See ratings by mood",
                command=self._toggle_mood_ratings
            )
            ratings_by_moood_button.grid(row=self._toggle_row, column=0)
        else:
            ttk.Label(
                master=self._frame,
                text="No ratings yet"
            ).grid(row=1, column=0, columnspan=2)
            row += 1
            self._toggle_row = row

        self._mood_frame = ttk.Frame(master=self._frame)
        self._mood_frame.grid(row=self._toggle_row + 1,
                              column=0, columnspan=5, sticky="w")
        self._mood_frame.grid_remove()

        back_button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._go_back
        )

        close_button = ttk.Button(
            master=self._frame,
            text="Close window",
            command=self._root.destroy
        )
        back_button.grid(row=self._toggle_row + 2, column=0)
        close_button.grid(row=self._toggle_row + 3,
                          column=0, pady=8, columnspan=10)

    def _toggle_mood_ratings(self):
        """Huolehtii, näytetäänkö arvostelut jotka on ryhmitelty fiiliksen perusteella, vai ei.
            Jos arvostelut ei ole esillä ja nappia painetaan, ne tulevat esiin ja toistepäin. """

        if self._mood_frame.winfo_ismapped():
            self._mood_frame.grid_remove()
        else:
            self._show_ratings_by_mood()
            self._mood_frame.grid()

    def _show_ratings_by_mood(self):
        """Näyttää arvostelut jaoteltuna moodin pohjalta
        """

        for widget in self._mood_frame.winfo_children():
            widget.destroy()

        row = 0

        if self._averages_by_mood:
            ttk.Label(
                master=self._mood_frame,
                text="Average ratings, when mood was:"
            ).grid(row=row, column=0, columnspan=2, sticky="w")

            row += 1

            for mood, ratings in self._averages_by_mood.items():
                mood_label = ttk.Label(
                    master=self._mood_frame,
                    text=f"{mood}", font=("Arial", 10, "bold")
                )
                mood_label.grid(row=row, column=0, sticky="w")

                row += 1

                for key in self._answer_keys:
                    ttk.Label(
                        master=self._mood_frame,
                        text=f"{key}: {ratings[key]}"
                    ).grid(row=row, column=0, sticky="w")
                    row += 1

                row += 1
        else:
            ttk.Label(
                master=self._mood_frame,
                text="No ratings yet"
            ).grid(row=1, column=0, columnspan=2)
