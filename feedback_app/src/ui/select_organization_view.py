from tkinter import ttk, constants


class SelectOrganizationView:
    def __init__(self, root, handle_org, org_repo, go_back):
        self._root = root
        self._handle_org = handle_org
        self._frame = None
        self._go_back = go_back
        self._org_repo = org_repo

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        ttk.Frame(self._frame, height=80).pack()

        style = ttk.Style()

        style.configure(
            "Org.TButton",
            font=("Arial", 11),
            padding=8
        )

        style.configure(
            "Back.TButton",
            font=("Arial", 10),
            padding=5
        )

        label = ttk.Label(
            master=self._frame,
            text="Select organization",
            font=("Arial", 14, "bold")
        )

        label.pack(pady=10)

        organization = self._org_repo.get_all()

        for org in organization:
            ttk.Button(
                master=self._frame,
                text=org.name,
                style="Org.TButton",
                width=25,
                command=lambda o=org: self._handle_org(o.org_id)
            ).pack(pady=3)

        ttk.Button(
            master=self._frame,
            text="Back",
            style="Back.TButton",
            command=self._go_back
        ).pack(pady=20)
