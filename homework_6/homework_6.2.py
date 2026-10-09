import json
try:
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)
    if not isinstance(users, list):
        raise ValueError("В JSON должен быть список пользователей")
    for user in users:
        if not isinstance(user, dict):
            raise ValueError("Пользователь должен быть словарём")
        login = user["login"]
        password = user["password"]
        expected = user["expected_result"]
        print("Логин:", login)
        print("Пароль:", password)
        print("Ожидаемый результат:", expected)
        print("--------------------")
except FileNotFoundError as e:
    print("Файл не найден:", e)
except json.JSONDecodeError as e:
    print("Ошибка чтения JSON:", e)
except KeyError as e:
    print("Отсутствует обязательное поле:", e)
except ValueError as e:
    print("Ошибка структуры данных:", e)