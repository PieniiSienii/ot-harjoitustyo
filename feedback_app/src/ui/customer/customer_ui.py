from ui.customer.mood_view import MoodView
from ui.customer.rating_view import RatingView
from ui.select_organization_view import SelectOrganizationView
from tkinter import ttk
from ui.view_flow import ViewFlow


class CustomerUI:
    def __init__(self, root, service, go_back):
        self._root = root
        self._service = service
        self._current_view = None
        self._mood = None
        self._org = None
        self._go_back = go_back

        self._flow = ViewFlow(root, on_empty_back=self._go_back)

    def start(self):
        self._show_org_view()

    def _show_org_view(self):
        self._flow.show(
            SelectOrganizationView(
            self._root,
            self._handle_org,
            self._flow.go_back
            )
        )

    def _handle_org(self, org_id):
        self._org_id = org_id
        self._show_mood_view()

    def _show_mood_view(self):
        self._flow.show(MoodView(
            self._root,
            self._handle_mood,
            self._flow.go_back
            )
        )

    def _handle_mood(self, mood):
        self._mood = mood
        self._show_rating()

    def _show_rating(self):
        self._flow.show(RatingView(
            self._root,
            self._handle_rating,
            self._flow.go_back
            )
        )

    def _handle_rating(self, rating):
        self._service.save_feedback(self._org_id, self._mood, rating)
        print("Thank you for your feedback!")
