from ui.customer.mood_view import MoodView
from ui.customer.questions_view import QuestionsView
from ui.select_organization_view import SelectOrganizationView
from ui.customer.end_view import EndView


class CustomerUI:
    def __init__(self, root, service, flow, go_back):
        self._root = root
        self._service = service
        self._current_view = None
        self._mood = None
        self._org_id = None
        self._go_back = go_back

        self._flow = flow
        self._flow._on_empty_back = self._go_back

    def start(self):
        self._show_org_view()

    def _show_org_view(self):
        self._flow.show(lambda:
                        SelectOrganizationView(
                            self._root,
                            self._handle_org,
                            self._go_back
                        )
                        )

    def _handle_org(self, org_id):
        self._org_id = org_id
        self._show_mood_view()

    def _show_mood_view(self):
        self._flow.show(lambda: MoodView(
            self._root,
            self._handle_mood,
            self._flow.go_back
        )
        )

    def _handle_mood(self, mood):
        self._mood = mood
        self._show_questions()

    def _show_questions(self):
        self._flow.show(lambda:
                        QuestionsView(
                            self._root,
                            self._handle_questions,
                            self._flow.go_back
                        )
                        )

    def _handle_questions(self, answers):
        self._service.save_feedback(self._org_id, self._mood, answers)
        self._show_end_view()

    def _show_end_view(self):
        self._flow.show(lambda: EndView(self._root))
