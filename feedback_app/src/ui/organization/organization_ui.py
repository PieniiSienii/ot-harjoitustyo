from ui.select_organization_view import SelectOrganizationView
from ui.organization.org_ratings_view import OrgRatingsView


class OrganizationUI:
    """ Vastaa organisaation näkymästä."""

    def __init__(self, root, service, flow, org_repo, go_back):
        self._root = root
        self._service = service
        self._current_view = None
        self._org = None
        self._go_back = go_back
        self._org_repo = org_repo
        self._flow = flow

    def start(self):
        self._show_org_view()

    def _show_org_view(self):
        """ Näyttää organisaation valintanäkymän. """

        self._flow.show(lambda:
                        SelectOrganizationView(
                            self._root,
                            self._handle_org,
                            self._org_repo,
                            self._go_back
                        )
                        )

    def _handle_org(self, org_id):
        """ Näyttää valitun organisaation arvostelunäkymän.

        Args:
            org_id: valitun organisaation id.
        """

        averages_by_mood = self._service.get_average_ratings_by_mood(org_id)
        averages = self._service.get_average_ratings(org_id)
        feedbacks = self._service.get_all()
        overall_rating = self._service.calc_overall_rating(org_id)
        get_status = self._service.get_rating_status(org_id)
        mood_difference = self._service.get_mood_differences(org_id)

        filtered_ratings = [fb for fb in feedbacks if fb.org_id == org_id]

        self._flow.show(lambda:
                        OrgRatingsView(
                            self._root,
                            filtered_ratings,
                            averages,
                            averages_by_mood,
                            overall_rating,
                            get_status,
                            mood_difference,
                            self._flow.go_back)
                        )
