from player import Player


class Captain(Player):
    def __init__(self, nick_name: str) -> None:
        super().__init__(nick_name)

    def set_nick_name(self, nick_name: str):
        self.nick_name = "captain " + nick_name
