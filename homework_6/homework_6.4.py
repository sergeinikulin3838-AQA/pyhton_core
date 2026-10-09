class InvalidTestStatusError(Exception):
    pass
def check_test_status(status):
    if status not in ["PASS", "FAIL", "SKIP"]:
        raise InvalidTestStatusError(f"Некорректный статус теста: {status}")
    return f"Статус {status} корректен"
statuses = ["PASS", "FAIL", "SKIP", "ERROR", "pass"]
for status in statuses:
    try:
        result = check_test_status(status)
        print(result)
    except InvalidTestStatusError as e:
        print("Ошибка:", e)