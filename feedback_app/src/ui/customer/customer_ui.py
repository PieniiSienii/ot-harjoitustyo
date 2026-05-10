from ui.customer.mood_view import MoodView
from ui.customer.questions_view import QuestionsView
from ui.select_organization_view import SelectOrganizationView
from ui.customer.end_view import EndView


class CustomerUI:
    """Class responsible for the customer feedback flow."""

    def __init__(self, root, service, flow, org_repo, go_back):
        """Constructor for the customer UI flow.

        Args:
            root: Tkinter root window.
            service: Feedback service object. 
            flow: ViewFlow object for naviagtion.
            org_repo: Repository containing organizations.
            go_back: Function for returning to the previous menu.
        """

        self._root = root
        self._service = service
        self._current_view = None
        self._mood = None
        self._org_id = None
        self._go_back = go_back
        self._org_repo = org_repo

        self._flow = flow

    def start(self):
        """Starts the customer feedback flow."""
        self._show_org_view()

    def _show_org_view(self):
        """Displays the organization selection view."""

        self._flow.show(lambda:
                        SelectOrganizationView(
                            self._root,
                            self._handle_org,
                            self._org_repo,
                            self._go_back
                        )
                        )

    def _handle_org(self, org_id):
        """Stores the selected organization id and moves to mood selection.

        Args:
            org_id: Selected organization id. 
        """

        self._org_id = org_id
        self._show_mood_view()

    def _show_mood_view(self):
        """Displays the mood selection view."""

        self._flow.show(lambda: MoodView(
            self._root,
            self._handle_mood,
            self._flow.go_back
        )
        )

    def _handle_mood(self, mood):
        """Stores the selected mood and moves to the questions view.

        Args:
            mood: Customer mood selection.
        """

        self._mood = mood
        self._show_questions()

    def _show_questions(self):
        """Displays the feedback questions view."""
        self._flow.show(lambda:
                        QuestionsView(
                            self._root,
                            self._handle_questions,
                            self._flow.go_back,
                            self._service
                        )
                        )

    def _handle_questions(self, answers):
        """Saves the feedback answers.

        Args:
            answers: List of question ratings on a scale of 1-5.
        """

        self._service.save_feedback(self._org_id, self._mood, answers)
        self._show_end_view()

    def _show_end_view(self):
        """Displays the final thank you view."""
        self._flow.show(lambda: EndView(self._root))
