import json
from pprint import pprint

flag = True

def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

def read(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        return json.load(file)

write(dict(), "phonebook.json")

while flag:
    print("1 - Получить контакт;")
    print("2 - Создать новый контакт;")
    print("3 - Выход из программы;")
    action = input()
    if action == "1":
        print("Введите имя контакта:")
        name = input()
        phonebook = read('phonebook.json')
        for key in phonebook:
            if key.startswith(name):
                print(key + " " + str(phonebook[key]))
            else:
                print("Такого контакта нет =(")
        print("Для продолжения нажмите 'Enter'")
        input()
    elif action == "2":
        print("Введите имя для нового контакта:")
        name = input()
        print("Введите номер для нового контакта:")
        phone = input()
        phonebook = read('phonebook.json')
        phonebook[name] = phone
        write(phonebook, 'phonebook.json')
        print("Контакт успешно сохранен / перезаписан!")
    elif action == "3":
        flag = False
