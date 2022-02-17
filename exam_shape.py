####################

class Shape:
    def __init__(self, name, area, hekef):
        self.name = name
        self._area = area
        self._hekef = hekef
    def __str__(self):
        return f'It is a {self.name} with area {self._area} and hekef {self._hekef}'

    def __repr__(self):
        return f'Shape(\'{self.name}\',\'{self._area}\',{self._hekef})'

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        if value > 0:
            self._area = value

    @property
    def hekef(self):
        return self._area

    @hekef.setter
    def hekef(self, value):
        if value > 0:
            self._hekef = value

sq = Shape('Square', 2, 2)

####################
