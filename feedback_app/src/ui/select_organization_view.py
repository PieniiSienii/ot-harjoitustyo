from tkinter import ttk, constants
from entities.organizations import ORGANIZATIONS


class SelectOrganizationView:
    def __init__(self, root, handle_org, go_back):
        self._root = root
        self._handle_org = handle_org
        self._frame = None
        self._go_back = go_back

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def hide(self):
        self._frame.pack_forget()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame,
                          text="Select organization")

        for i, org in enumerate(ORGANIZATIONS):
            ttk.Button(
                master=self._frame,
                text=org.name,
                command=lambda o=org: self._handle_org(o.org_id)
            ).grid(row=i+1, column=0)

        ttk.Button(
            master=self._frame,
            text="Back",
            command=self._go_back
        ).grid(row=len(ORGANIZATIONS) + 1, column=0)