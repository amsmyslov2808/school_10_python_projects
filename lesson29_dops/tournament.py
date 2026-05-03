from decorators import log_action

from participant import Participant


class Tournament:
    _participants: list[Participant]

    def __init__(self):
        self._participants = []

    def add_participant(self, participant):
        self._participants.append(participant)

    def show_participant(self):
        for participant_noumber in range(len(self._participants)):
            print(f"{participant_noumber+1}. {self._participants[participant_noumber]}")

    def find_participant(self, name: str):
        objec = None
        for participaint in self._participants:
            if participaint.name == name:
                objec = participaint
                break
        return objec

    def find_participant(self, name: str):
        for participaint in self._participants:
            if participaint.name == name:
                return participaint

        return None

    def add_points_to_parcticipant(self, name: str, points: int):
        self.find_participant(name).add_points(points)

    def remove_points_to_participant(self, name: str, points: int):
        self.find_participant(name).remove_points(points)

    def show_rating(self):
        print("Рейтинг турнира:")
        print()

        parcticants = sorted(self._participants, key=lambda u: u._score, reverse=True)

        print(f"1. {parcticants[0].name} - {parcticants[0]._score} баллов")
        print(f"2. {parcticants[1].name} - {parcticants[1]._score} баллов")
        print(f"3. {parcticants[2].name} - {parcticants[2]._score} баллов")

    def get_winner(self):
        parcticants = sorted(self._participants, key=lambda u: u._score, reverse=True)
        return parcticants[0]

    def show_debug_info(self):
        for participant in self._participants:
            print(participant.__dict__)

    def __len__(self):
        return len(self._participants)
