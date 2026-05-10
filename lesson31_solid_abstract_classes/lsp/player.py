class Player:
    nick_name: str

    def __init__(self, nick_name: str) -> None:
        self.nick_name = nick_name

    def set_nick_name(self, nick_name: str):
        self.nick_name = nick_name

    def print_info(self):
        print(f"ник: {self.nick_name}")
