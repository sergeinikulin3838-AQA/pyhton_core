import random
tests = [
    "test_login",
    "test_logout",
    "test_registration",
    "test_profile",
    "test_payment",
    "test_search"
]
count = int(input("Введите количество тестов для запуска: "))
if count > len(tests):
    print("Ошибка: такого количества тестов нет.")
else:
    selected_tests = random.sample(tests, count)
    statuses = ["PASS", "FAIL", "SKIP"]
    for test in selected_tests:
        status = random.choice(statuses)
        print(test, "-", status)