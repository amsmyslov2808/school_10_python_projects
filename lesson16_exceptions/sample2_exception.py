try:
    file_in = open("test.txt")

    try:
        line = file_in.readline()
    except:
        print("программа будет закрыта. невозможно считать линию в файле")

    file_in.close()
except:
    print("программа будет закрыта. файл test.txt в директории не обнаружен")
