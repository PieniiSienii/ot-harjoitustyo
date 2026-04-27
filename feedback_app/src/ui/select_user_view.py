from tkinter import ttk, constants


class SelectUserView:
    def __init__(self, root, handle_customer, handle_admin):
        self._root = root
        self._handle_customer = handle_customer
        self._handle_admin = handle_admin

        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
                          text="Welcome to Feedback App")

        admin_button = ttk.Button(master=self._frame,
                                  text="Organization",
                                  command=self._handle_admin)
        customer_button = ttk.Button(master=self._frame,
                                     text="Customer",
                                     command=self._handle_customer)

        label.grid(row=0, column=0, columnspan=2)
        admin_button.grid(row=1, column=0)
        customer_button.grid(row=1, column=1)

        close_button = ttk.Button(
            master=self._frame,
            text="Close window",
            command=self._root.destroy
        )
        close_button.grid(row=3, column=0, pady=8)
