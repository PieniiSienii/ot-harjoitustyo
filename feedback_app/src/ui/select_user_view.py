from tkinter import ttk, constants


class SelectUserView:
    """Class responsible for selecting the user."""

    def __init__(self, root, handle_customer, handle_admin):
        self._root = root
        self._handle_customer = handle_customer
        self._handle_admin = handle_admin

        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        ttk.Frame(self._frame, height=80).pack()
        label = ttk.Label(master=self._frame,
                          text="Hello! Select your role:", font=("Arial", 16, "bold"), justify="center"
                          )

        label.pack(pady=10)

        button_frame = ttk.Frame(master=self._frame)
        button_frame.pack(pady=5)

        admin_button = ttk.Button(
            master=button_frame,
            text="Organization",
            command=self._handle_admin
        )

        customer_button = ttk.Button(
            master=button_frame,
            text="Customer",
            command=self._handle_customer
        )

        admin_button.pack(side="left", padx=5)
        customer_button.pack(side="left", padx=5)

        close_button = ttk.Button(
            master=self._frame,
            text="Close window",
            command=self._root.destroy
        )
        close_button.pack(pady=12)
