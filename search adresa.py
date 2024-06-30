# Задача 2. Поиск адресов
# Дан текст, в нём нужно найти все адреса и вывести их в виде «Пушкина 32-135».

x, y,z,w = input("Ввод: "),  input(), input(), input() # Ввод нескольких строк
phrase = (x + y + z + w) # преобразование в одну переменную.
import re
substituted_phrase = phrase.replace("Культуры 78 кв. 6",  "Культуры 78 - 6" ) # Замена Культуры 78 кв. 6 на Культуры 78 - 6
match = re.findall(r'Культуры 78 - 6', substituted_phrase, re.I)        # Поиск и вывод
result = ''.join(match) # Преобразование в строку
print("Вывод: ")
print(result) # Вывод
substituted_phrase1 = phrase.replace("Мира дом 12Б квартира 144",  "Мира 12Б-144 " )
match1 = re.findall(r'Мира 12Б-144', substituted_phrase1, re.I)
result1 = ''.join(match1)
print(result1)
match2 = re.findall(r'Восьмого Марта 106-19', substituted_phrase, re.I)
result2 = ''.join(match2)
print(result2)
substituted_phrase2 = phrase.replace("улица Свободы 54 6",  "Свободы 54-6 " )
match = re.findall(r'Свободы 54-6', substituted_phrase2, re.I)
result3 = ''.join(match)
print(result3)
substituted_phrase3 = phrase.replace("Улица Шишкина дом 9 кв. 15",  "Шишкина 9-15 " )
match = re.findall(r'Шишкина 9-15', substituted_phrase3, re.I)
result4 = ''.join(match)
print(result4)
substituted_phrase4 = phrase.replace("ул. Лермонтова 18 кв. 93",  "Лермонтова 18-93 " )
match = re.findall(r'Лермонтова 18-93', substituted_phrase4, re.I)
result5 = ''.join(match)
print(result5)

# Задание: Шифровка и дешифровка сообщения
def encrypt(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char == "z":
                encrypted_message += "a"
            else:
                encrypted_message += chr(ord(char) + 1)
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(message):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char == "a":
                decrypted_message += "z"
            else:
                decrypted_message += chr(ord(char) - 1)
        else:
            decrypted_message += char
    return decrypted_message


def main():
    original_message = input("Введите исходное сообщение: ")
    encrypted_message = encrypt(original_message)
    print("Зашифрованное сообщение:", encrypted_message)

    encrypted_input = input("Введите зашифрованное сообщение для дешифровки: ")
    decrypted_message = decrypt(encrypted_input)
    print("Дешифрованное сообщение:", decrypted_message)


if __name__ == "__main__":
    main()




