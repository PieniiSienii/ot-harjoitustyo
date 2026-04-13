from ui.customer.mood_view import MoodView
from ui.customer.rating_view import RatingView


class CustomerUI:
    def __init__(self, root, service):
        self._root = root
        self._service = service
        self._current_view = None
        self._mood = None

    def start(self):
        self._show_mood_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

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
        self._service.save_feedback(self._mood, rating)
        print("Thank you for your feedback!")
