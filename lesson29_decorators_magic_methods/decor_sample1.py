# def func_ext():
#     print("до функции")
#     hello()
#     print("после функции")


# def decorator(func):
#     def wrapper():
#         print("до функции")
#         func()
#         print("после функции")

#     return wrapper


# @decorator
# def hello():
#     print("hello")


# new_hello = decorator(hello)
# new_hello()

# func_ext()


def email_validator(func):
    def wrapper(email: str):
        if email.find("@") == -1:
            raise Exception("Ошибка. Нет знака собачка.")
        else:
            func(email)

    return wrapper


@email_validator
def send_email(email: str):
    print(f"SEND TO {email}")


@email_validator
def recieve_email(email: str):
    print(f"RECIEVE TO {email}")


# def send_email(email: str):
#     if email.find("@") == -1:
#         raise Exception("Ошибка. Нет знака собачка.")
#     else:
#         print(f"SEND TO {email}")

email = "a.m.smyslov@yandex.ru"
send_email(email)
recieve_email(email)
