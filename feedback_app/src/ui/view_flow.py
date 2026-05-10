class ViewFlow:
    """Class responsible for managing views and navigation between them.

    Stores previously shown view factories in history so they
    can be recreated when navigating backwards.
    """

    def __init__(self, root,):
        """Constructor for the view manager.

        Args:
            root: Tkinter root window.
        """

        self._root = root
        self._history = []
        self._current_view = None
        self._current_factory = None

    def show(self, view):
        """Displays a new view and stores the previous one in history.

        Args:
            view: Callable that creates and returns a view object.
        """

        if self._current_view is not None:
            self._current_view.destroy()
            self._history.append(self._current_factory)

        self._current_factory = view
        self._current_view = view()
        self._current_view.pack()
        self._root.update()

    def clear(self):
        """Removes the current view and clears the navigation history."""

        if self._current_view is not None:
            self._current_view.destroy()
            self._current_view = None
        self._history = []

    def go_back(self):
        """Returns to the previous view."""

        if self._current_view is not None:
            self._current_view.destroy()

        if not self._history:
            return

        self._current_factory = self._history.pop()
        self._current_view = self._current_factory()
        self._current_view.pack()
        self._root.update()
