from session import Session


class Cinema:
    __name: str
    __sessions: list[Session]

    def __init__(self, name: str):
        self.__name = name
        self.__sessions = []

    def add_session(self, session: Session) -> None:
        pass

    def show_sessions(self) -> list[str]:
        returned_sessions: list[str] = []

        for current_session in self.__sessions:
            returned_sessions.append(current_session.get_info())

        return returned_sessions
