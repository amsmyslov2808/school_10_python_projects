# f = None
# try:
#     f = open("aaa.txt", "r")
# except:
#     print("file not found")
# finally:
#     if f:
#         f.close()


try:
    with open("aaa.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("file not found")
