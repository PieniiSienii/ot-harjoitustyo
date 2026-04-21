class ViewFlow:
    def __init__(self, root, on_empty_back= None):
        self._root = root
        self._history = []
        self._current_view = None
        self._on_empty_back = on_empty_back
    
    def show(self, view):
        if self._current_view is not None:
            self._current_view.hide()
            self._history.append(self._current_view)
        self._current_view = view
        self._current_view.pack()

    def go_back(self):
        if not self._history:
            if self._on_empty_back:
                self._on_empty_back()
            return
        self._current_view.destroy()
        self._current_view = self._history.pop()
        self._current_view.pack()
