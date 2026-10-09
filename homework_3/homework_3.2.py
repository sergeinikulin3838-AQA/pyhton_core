test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]
def print_report(test_cases, statuses):
    pass_count = 0
    fail_count = 0
    for test_case, status in zip(test_cases, statuses):
        print(test_case, "-", status)
        if status == "PASS":
            pass_count += 1
        elif status == "FAIL":
            fail_count += 1
    print("Успешных тестов:", pass_count)
    print("Неуспешных тестов:", fail_count)
    if fail_count > 0:
        print("Запуск неуспешный")
    else:
        print("Запуск успешный")
print_report(test_cases, statuses)