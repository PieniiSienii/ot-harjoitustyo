from ui.select_user_view import SelectUserView
from ui.customer.customer_ui import CustomerUI
from ui.admin.admin_ui import AdminUI
from ui.view_flow import ViewFlow


class UI:
    def __init__(self, root, service, org_repo):
        self._root = root
        self._service = service
        self._org_repo = org_repo
        self._flow = ViewFlow(root)

    def start(self):
        self._show_select_user()

    def _show_select_user(self):
        self._flow.show(lambda:
                        SelectUserView(
                            self._root,
                            self._show_customer,
                            self._show_admin
                        )
                        )

    def _show_customer(self):
        self._flow.clear()
        CustomerUI(
            self._root,
            self._service,
            self._flow,
            self._show_select_user
        ).start()

    def _show_admin(self):
        self._flow.clear()
        AdminUI(
            self._root,
            self._service,
            self._flow,
            self._org_repo,
            self._show_select_user
        ).start()
