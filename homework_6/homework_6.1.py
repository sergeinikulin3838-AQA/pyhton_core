from functools import reduce
tests = [
    {"name": "test_login", "status": "PASS", "duration": 1.5},
    {"name": "test_logout", "status": "FAIL", "duration": 2.0},
    {"name": "test_registration", "status": "PASS", "duration": 3.5},
    {"name": "test_profile", "status": "SKIP", "duration": 0},
    {"name": "test_payment", "status": "FAIL", "duration": 4.0}
]
failed_tests = list(filter(lambda test: test["status"] == "FAIL", tests))
failed_names = list(map(lambda test: test["name"], failed_tests))
passed_names = [test["name"] for test in tests if test["status"] == "PASS"]
skipped_tests = [test for test in tests if test["status"] == "SKIP"]
total_time = reduce(lambda total, test: total + test["duration"], tests, 0)
print("PASS:", len(passed_names))
print("FAIL:", len(failed_names))
print("SKIP:", len(skipped_tests))
print("Упавшие тесты:", failed_names)
print("Успешные тесты:", passed_names)
print("Общее время:", total_time, "сек.")