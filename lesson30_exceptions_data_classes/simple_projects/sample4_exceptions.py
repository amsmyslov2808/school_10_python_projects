class MyError(Exception):
    pass


class EmptyField(MyError):
    pass


try:
    a = input("a: ")
    if a == " ":
        raise EmptyField("Поле не может быть пустым")
except EmptyField as e:
    print(f"Ошибка. {e}")
except Exception as e:
    print(f"Общая ошибка. {e}")
