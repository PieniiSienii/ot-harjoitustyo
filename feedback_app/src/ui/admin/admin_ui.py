from ui.select_organization_view import SelectOrganizationView
from ui.admin.org_ratings_view import OrgRatingsView
from ui.view_flow import ViewFlow

class AdminUI:
    def __init__(self, root, service, go_back):
        self._root = root
        self._service = service
        self._current_view = None
        self._org = None
        self._go_back = go_back
        self._flow = ViewFlow(root, on_empty_back=self._go_back)

    def start(self):
        self._show_org_view()

    def _show_org_view(self):
        self._flow.show(lambda:
            SelectOrganizationView(
            self._root,
            self._handle_org,
            self._flow.go_back
            )
        )

    def _handle_org(self, org_id):
        feedbacks = self._service.get_all()

        filtered_ratings = []
        for feedback in feedbacks:
            if feedback.org_id == org_id:
                filtered_ratings.append(feedback)

        self._flow.show(
            OrgRatingsView(self._root, filtered_ratings, self._show_org_view)
        )
