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
        self._frame.pack(fill=constants.X, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame,
                          text="Select organization")
        label.grid(row=0, column=0)

        organization = self._org_repo.get_all()
        for i, org in enumerate(organization):
            ttk.Button(
                master=self._frame,
                text=org.name,
                command=lambda o=org: self._handle_org(o.org_id)
            ).grid(row=i+1, column=0)

        ttk.Button(
            master=self._frame,
            text="Back",
            command=self._go_back
        ).grid(row=len(organization) + 2, column=0, pady=8)
