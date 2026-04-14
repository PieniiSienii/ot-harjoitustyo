from ui.select_organization_view import SelectOrganizationView
from ui.admin.org_ratings_view import OrgRatingsView


class AdminUI:
    def __init__(self, root, service):
        self._root = root
        self._service = service
        self._current_view = None
        self._org = None

    def start(self):
        self._show_org_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_org_view(self):
        self._hide_current_view()

        self._current_view = SelectOrganizationView(
            self._root,
            self._handle_org
        )
        self._current_view.pack()

    def _handle_org(self, org_id):
        self._hide_current_view()

        feedbacks = self._service.get_all()

        filtered_ratings = []
        for feedback in feedbacks:
            if feedback["org_id"] == org_id:
                filtered_ratings.append(feedback)

        self._current_view = OrgRatingsView(self._root, filtered_ratings)
        self._current_view.pack()
