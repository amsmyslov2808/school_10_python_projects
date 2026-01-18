# 1. задать алфавит
# 2. выбрать режим работы (шифрование/дешифрование)
# 3. ввести шифруемую/дешифруемую строку
# 4. ввести ключ шифрования/дешифрования
# 5. вывести обработанную строку

ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789.,;:!?-() "


def crypt_string(original_string, key):
    result_string = ""

    for item in original_string:
        index_in_alphabet = ALPHABET.find(item)

        if index_in_alphabet == -1:
            result_string += item
        else:
            new_index = (index_in_alphabet + key) % len(ALPHABET)
            result_string += ALPHABET[new_index]

    return result_string


def encrypt_string(original_string, key):
    return crypt_string(original_string, key)


def decrypt_string(original_string, key):
    return crypt_string(original_string, -key)


operating_mode = int(
    input("введите номер режима работы 1 - шифрование, 2 - дешифрование строки: ")
)

original_string = input("введите исходную строку: ")
key = int(input("введите ключ: "))

result_string = ""

if operating_mode == 1:
    result_string = encrypt_string(original_string, key)
elif operating_mode == 2:
    result_string = decrypt_string(original_string, key)

print(f"результирующая строка = {result_string}")
