import random as rnd

_PYTHONESS_COUNT = 3
_GUESS_MIN = 10
_GUESS_MAX = 99


class Pythoness:
    def __init__(self, index: int):
        self.index = index
        self.guess = 0
        self.confidence_level = 0
        self.history = []  # selected numbers in selection order

    def update(self):
        self.guess = rnd.randint(_GUESS_MIN, _GUESS_MAX)

    def result(self, selected_number: int):
        if self.guess == selected_number:
            self.confidence_level += 1
        else:
            self.confidence_level -= 1
        self.history.append(self.guess)  # store last guess


class User:
    def __init__(self):
        self.history = []  # selected numbers in selection order

    def add_number(self, selected_number: int):
        self.history.append(selected_number)


class Model:
    def __init__(self):
        self.user = User()
        self.pythonesses = []  # list of Pythoness instances
        i = 0
        while i < _PYTHONESS_COUNT:
            self.pythonesses.append(Pythoness(i))
            i += 1

    def update(self):
        for pythoness in self.pythonesses:
            pythoness.update()

    def result(self, user_selected_number: int):
        self.user.add_number(user_selected_number)
        for pythoness in self.pythonesses:
            pythoness.result(user_selected_number)

    @property
    def guess_min(self) -> int:
        return _GUESS_MIN

    @property
    def guess_max(self) -> int:
        return _GUESS_MAX
