import json


class User:
    def __init__(self, name, password, handler):
        self.password = password
        self.handler = handler
        self.name = name
        self.is_write = False


    def read(self):
        data = self.handler.read()
        for note in data:
            print(f"{note['user']}: {note['text']}")

    def write(self):
        if self.is_write:
            text = input("Введите текст заметки:\n")
            self.handler.write({
                'user': self.name,
                'text': text
            })
            print("Запись добавлена!")
        else:
            print("Вам не доступна запись!")



class FileHandler:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, "r", encoding='utf-8') as file:
            data = json.load(file)
        return data

    def write(self, note):
        data = self.read()
        data.append(note)
        with open(self.path, "r", encoding='utf-8') as file:
            json.dump(file, note, ensure_ascii=False)


def main():
    handler = FileHandler("file.json")
    sasha = User("Саша", "1234", handler)
    vova = User("Вова", "4321", handler)
    users = [sasha, vova]
    print("Введите имя")
    user_input = input()
    current_user = ""
    for user in users:
        if user_input == user.name:
            current_user = user
            break
    if not current_user:
        print("Нет такого пользователя")
        exit()
    print("Введите пароль")
    user_input = input()
    if user_input != current_user.password:
        print("Неверный пароль!")
        exit()
    current_user.read()


if __name__ == "__main__":
    main()
