from ui.select_user_view import SelectUserView
from ui.customer.customer_ui import CustomerUI
from ui.organization.organization_ui import OrganizationUI
from ui.view_flow import ViewFlow


class UI:
    """Main class responsible for controlling the application UI."""

    def __init__(self, root, service, org_repo):
        """Constructor for the UI controller.

        Args:
            root: Tkinter root window.
            service: Feedback service object.
            org_repo: Organization repository.
        """

        self._root = root
        self._service = service
        self._org_repo = org_repo
        self._flow = ViewFlow(root)

    def start(self):
        """Starts the application UI."""

        self._show_select_user()

    def _show_select_user(self):
        """Shows the user role selection view"""

        self._flow.show(lambda:
                        SelectUserView(
                            self._root,
                            self._show_customer,
                            self._show_organization
                        )
                        )

    def _show_customer(self):
        """Shows the customer view."""

        self._flow.clear()
        CustomerUI(
            self._root,
            self._service,
            self._flow,
            self._org_repo,
            self._show_select_user
        ).start()

    def _show_organization(self):
        """Shows the organization view."""

        self._flow.clear()
        OrganizationUI(
            self._root,
            self._service,
            self._flow,
            self._org_repo,
            self._show_select_user
        ).start()
