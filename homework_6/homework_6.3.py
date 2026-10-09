def check_settings(retries, timeout):
    if not isinstance(retries, int) or retries < 0 or retries > 5:
        raise ValueError("Количество повторных запусков должно быть от 0 до 5")
    if not isinstance(timeout, (int, float)) or timeout <= 0:
        raise ValueError("Таймаут должен быть положительным числом")
    return "Настройки корректны"
test_data = [
    (3, 10),
    (2, -5),
    (7, 10)
]
for retries, timeout in test_data:
    try:
        result = check_settings(retries, timeout)
        print(result)
    except ValueError as e:
        print("Ошибка:", e)