class ViewFlow:
    """Luokka, joka hallitsee näkymiä ja niissä navigointia.
        Säilyttää historiassa factory-funktiot näkymistä, jotta back-navigaatiossa ne voidaan luoda uudelleen."""

    def __init__(self, root,):
        self._root = root
        self._history = []
        self._current_view = None
        self._current_factory = None

    def show(self, view):
        """Näyttää uuden näkymän ja tallentaa edellsen historiaan.

        Args:
            view: Kutsuttava näkymä, joka luodaan ja tallennetaan historiaan.
        """
        if self._current_view is not None:
            self._current_view.destroy()
            self._history.append(self._current_factory)

        self._current_factory = view
        self._current_view = view()
        self._current_view.pack()
        self._root.update()

    def clear(self):
        """Poistaa nykyisen näkymän ja tyhjentää historian. """

        if self._current_view is not None:
            self._current_view.destroy()
            self._current_view = None
        self._history = []

    def go_back(self):
        """ Palaa edelliseen näkymään. """

        if self._current_view is not None:
            self._current_view.destroy()

        if not self._history:
            return

        self._current_factory = self._history.pop()
        self._current_view = self._current_factory()
        self._current_view.pack()
        self._root.update()
