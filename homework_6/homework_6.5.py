import json
from functools import reduce
try:
    with open("tests.json", "r", encoding="utf-8") as file:
        tests = json.load(file)
    if not isinstance(tests, list) or len(tests) == 0:
        raise ValueError("В JSON должен быть непустой список тестов")
    for test in tests:
        if not isinstance(test, dict):
            raise ValueError("Каждый тест должен быть словарём")
        if "name" not in test or "status" not in test or "duration" not in test:
            raise ValueError("У теста отсутствуют обязательные поля")
        if not isinstance(test["name"], str) or not test["name"]:
            raise ValueError("Некорректное название теста")
        if test["status"] not in ["PASS", "FAIL", "SKIP"]:
            raise ValueError("Некорректный статус теста")
        if type(test["duration"]) not in (int, float) or test["duration"] < 0:
            raise ValueError("Некорректное время выполнения")
    passed = [test for test in tests if test["status"] == "PASS"]
    failed = list(filter(lambda test: test["status"] == "FAIL", tests))
    skipped = [test for test in tests if test["status"] == "SKIP"]
    failed_names = [test["name"] for test in failed]
    longest_test = max(tests, key=lambda test: test["duration"])
    total_time = reduce(lambda total, test: total + test["duration"], tests, 0)
    report = {
        "total_tests": len(tests),
        "passed": len(passed),
        "failed": len(failed),
        "skipped": len(skipped),
        "failed_tests": failed_names,
        "longest_test": longest_test["name"],
        "total_duration": total_time
    }
    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=4)
    print("Отчёт успешно создан")
    print(json.dumps(report, ensure_ascii=False, indent=4))
except FileNotFoundError as e:
    print("Файл не найден:", e)
except json.JSONDecodeError as e:
    print("Некорректный JSON:", e)
except (ValueError, TypeError, KeyError) as e:
    print("Ошибка данных:", e)
except OSError as e:
    print("Ошибка работы с файлом:", e)