from tkinter import ttk, constants
from entities.organizations import ORGANIZATIONS


class SelectOrganizationView:
    def __init__(self, root, handle_org):
        self._root = root
        self._handle_org = handle_org
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text="Select organization")
        for org in ORGANIZATIONS:
            ttk.Button(
                master=self._frame,
                text=org.name,
                command=lambda o=org: self._handle_org(o.id)
            ).grid(row=1, column=org.id)
