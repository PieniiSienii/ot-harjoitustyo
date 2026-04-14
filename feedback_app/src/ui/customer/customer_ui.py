from ui.customer.mood_view import MoodView
from ui.customer.rating_view import RatingView
from ui.select_organization_view import SelectOrganizationView


class CustomerUI:
    def __init__(self, root, service):
        self._root = root
        self._service = service
        self._current_view = None
        self._mood = None
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
        self._org_id = org_id
        self._show_mood_view()

    def _show_mood_view(self):
        self._hide_current_view()

        self._current_view = MoodView(
            self._root,
            self._handle_mood
        )
        self._current_view.pack()

    def _handle_mood(self, mood):
        self._mood = mood
        self._show_rating()

    def _show_rating(self):
        self._hide_current_view()

        self._current_view = RatingView(
            self._root,
            self._handle_rating
        )
        self._current_view.pack()

    def _handle_rating(self, rating):
        self._service.save_feedback(self._org_id, self._mood, rating)
        print("Thank you for your feedback!")
