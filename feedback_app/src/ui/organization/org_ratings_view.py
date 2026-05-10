from tkinter import ttk, constants


class OrgRatingsView:
    """Luokka, joka vastaa organisaation arvostelunäkymästä"""

    def __init__(self, root, feedbacks, averages, averages_by_mood, overall_rating, get_status, get_mood_difference, go_back):
        self._root = root
        self._feedbacks = feedbacks
        self._averages = averages
        self._averages_by_mood = averages_by_mood
        self._overall_rating = overall_rating
        self._get_status = get_status
        self._mood_difference = get_mood_difference
        self._go_back = go_back
        self._frame = None
        self._mood_frame = None
        self._answer_keys = ["Cleanliness",
                             "Customer Service", "Would Recommend"]

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._frame.grid_columnconfigure(0, weight=1)

        label = ttk.Label(
            master=self._frame,
            text="Organization feedbacks",
            font=("Arial", 16, "bold"),
            anchor="center"
        )
        label.grid(row=0, column=0, pady=(5, 10), sticky="ew")

        self.show_overall_rating()

        container = ttk.Frame(self._frame)
        container.grid(row=3, column=0, pady=10, sticky="ew")

        container.grid_columnconfigure(0, weight=1, uniform="cols")
        container.grid_columnconfigure(1, weight=1, uniform="cols")

        self.left = ttk.Frame(container)

        if self._mood_difference:
            self.left.grid(row=0, column=0, padx=20)

            self.right = ttk.Frame(container)
            self.right.grid(row=0, column=1, padx=20)
        else:
            self.left.grid(row=0, column=0, columnspan=2)

        self.show_status()
        self.show_ratings()
        self.get_difference()

        self._mood_frame = ttk.Frame(
            master=self._frame,
            padding=10
        )

        button_frame = ttk.Frame(self._frame)
        button_frame.grid(row=6, column=0, pady=15)

        back_button = ttk.Button(
            master=button_frame,
            text="Back",
            command=self._go_back
        )

        close_button = ttk.Button(
            master=button_frame,
            text="Close window",
            command=self._root.destroy
        )
        back_button.pack(side="left", padx=10)
        close_button.pack(side="left", padx=10)

    def show_ratings(self):
        row = 0

        if self._averages:
            ttk.Label(
                master=self.left,
                text="Averages",
                font=("Arial", 12, "bold")
            ).grid(
                row=row, column=0, pady=10, sticky="n")

            row += 1

            for key in self._answer_keys:
                ttk.Label(
                    master=self.left,
                    text=f"{key} {self._averages[key]:.2f}"
                ).grid(row=row, column=0, pady=5, sticky="n")
                row += 1

            self._toggle_button = ttk.Button(
                master=self._frame,
                text="Show ratings by mood ▼",
                command=self._toggle_mood_ratings
            )

            self._toggle_button.grid(row=4, column=0, pady=10)

        else:
            ttk.Label(
                master=self._frame,
                text="No ratings yet"
            ).grid(row=1, column=0, pady=5)
            row += 1
            self._toggle_row = row

    def _toggle_mood_ratings(self):
        """Huolehtii, näytetäänkö arvostelut jotka on ryhmitelty fiiliksen perusteella, vai ei.
            Jos arvostelut ei ole esillä ja nappia painetaan, ne tulevat esiin ja toistepäin. """

        if self._mood_frame.winfo_ismapped():
            self._mood_frame.grid_remove()
            self._toggle_button.config(text="Show ratings by mood ▼")
        else:
            self._show_ratings_by_mood()
            self._mood_frame.grid(row=5, column=0, pady=10)
            self._toggle_button.config(text="Hide ratings by mood ▲")

    def _show_ratings_by_mood(self):
        """Näyttää arvostelut jaoteltuna moodin pohjalta
        """

        for widget in self._mood_frame.winfo_children():
            widget.destroy()

        row = 0

        if self._averages_by_mood:
            ttk.Label(
                master=self._mood_frame,
                text="Average ratings, when mood was:",
                font=("Arial", 12, "bold")
            ).grid(row=row, column=0, pady=5)

            row += 1

            for mood, ratings in self._averages_by_mood.items():
                mood_label = ttk.Label(
                    master=self._mood_frame,
                    text=f"{mood}",
                    font=("Arial", 11, "bold")
                )
                mood_label.grid(row=row, column=0, pady=5)
                row += 1

                for key in self._answer_keys:
                    ttk.Label(
                        master=self._mood_frame,
                        text=f"{key}: {ratings[key]:.2f}"
                    ).grid(row=row, column=0, pady=5)
                    row += 1

                row += 1
        else:
            ttk.Label(
                master=self._mood_frame,
                text="No ratings yet"
            ).grid(row=1, column=0, pady=5)

    def show_overall_rating(self):
        if self._overall_rating:
            ttk.Label(
                master=self._frame,
                text=f"Overall Rating: {self._overall_rating:.2f}",
                font=("Arial", 12, "bold")
            ).grid(row=1, column=0, pady=(0, 10))
        else:
            pass

    def show_status(self):
        if self._get_status:
            ttk.Label(
                master=self._frame,
                text=f"Status: {self._get_status}",
                font=("Arial", 12, "bold")
            ).grid(row=2, column=0, pady=(0, 5))

    def get_difference(self):
        if self._mood_difference:
            ttk.Label(
                master=self.right,
                text="Rating change (Excellent vs Bad):",
                font=("Arial", 12, "bold")
            ).grid(row=3, column=0, pady=10)

            row = 4
            for key, diff in self._mood_difference.items():
                if diff > 0:
                    text = f"- {key}: +{diff}"

                else:
                    text = f"- {key}: {diff}"

                ttk.Label(
                    master=self.right,
                    text=text,
                    font=("Arial", 10)
                ).grid(row=row, column=0, pady=5)
                row += 1
