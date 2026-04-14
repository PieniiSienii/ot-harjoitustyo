from ui.select_user_view import SelectUserView
from ui.customer.customer_ui import CustomerUI
from ui.admin.admin_ui import AdminUI


class UI:
    def __init__(self, root, service):
        self._root = root
        self._service = service
        self._current_view = None

    def start(self):
        self._show_select_user()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_select_user(self):
        self._hide_current_view()

        self._current_view = SelectUserView(
            self._root,
            self._show_customer,
            self._show_admin
        )

        self._current_view.pack()

    def _show_customer(self):
        self._hide_current_view()

        self._current_view = CustomerUI(
            self._root,
            self._service
        )

        self._current_view.start()

    def _show_admin(self):
        self._hide_current_view()

        self._current_view = AdminUI(
            self._root,
            self._service
        )

        self._current_view.start()
