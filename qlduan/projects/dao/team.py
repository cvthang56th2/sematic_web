class Team:
    _id = None
    _name = None
    _nhanviens = []
    _duans = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def duans(self):
        return self._duans

    @duans.setter
    def duans(self, value):
        self._duans = value

    @property
    def nhanviens(self):
        return self._nhanviens

    @nhanviens.setter
    def nhanviens(self, value):
        self._nhanviens = value
