def log_action(function):
    def wrapper():
        print(f"[LOG] Выполняется действие: {function.__name__}")
        function()
    return wrapper
@log_action
def pr():
    print("print")
pr()