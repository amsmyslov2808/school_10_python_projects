class Participant:
    name: str
    school_class: str
    _score: int

    def __init__(self, name: str, school_class: str):
        self.name = name
        self.school_class = school_class
        self._score = 0

    def add_points(self, points: int):
        if points > 0:
            self._score += points

    def remove_points(self, points: int):
        self._score -= points

    def get_role(self):
        return "Участник"

    def __str__(self):
        return f"{self.name}, {self.school_class} класс - {self._score} баллов, роль: {self.get_role()}"

    def __repr__(self):
        return f"Participant(name='{self.name!r}', school_class='{self.school_class}', score={self._score})"
