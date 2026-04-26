class MyBot:
    __handlers: dict

    def __init__(self):
        self.__handlers = {}

    def message_handler(self, command: str):
        def wrapper(func):
            self.__handlers[command] = func
            return func

        return wrapper

    def recieve_message(self, command: str):
        if command in self.__handlers:
            self.__handlers[command]()
        else:
            print("неизвестная команда")


bot = MyBot()


@bot.message_handler("/start")
def start():
    print("отработала команда /start")


@bot.message_handler("/help")
def help():
    print("отработала команда /help")


# dict1 = {}
# dict1["/start"] = start
# dict1["/help"] = help

# dict1["/start"]()
# dict1["/help"]()

# bot.recieve_message("/start")
# bot.recieve_message("/help")
# bot.recieve_message("/time")
