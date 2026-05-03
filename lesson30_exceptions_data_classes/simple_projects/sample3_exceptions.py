def func1():
    try:
        return 1 / 0
    except:
        return 0


def func2():
    return func1()


# try:
#     res = func2()
#     print(res)
# except:
#     print("Ошибка при вызове func2")
res = func2()
print(res)
