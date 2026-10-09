text = input("Введите результаты тестов через пробел: ")
results = text.split()
def get_test_statistics(results):
    statistics = {
        "PASS": 0,
        "FAIL": 0,
        "SKIP": 0
    }
    for result in results:
        if result == "PASS":
            statistics["PASS"] += 1
        elif result == "FAIL":
            statistics["FAIL"] += 1
        elif result == "SKIP":
            statistics["SKIP"] += 1
    return statistics
result = get_test_statistics(results)
success_percent = result["PASS"] / len(results) * 100
print("Всего тестов:", len(results))
print("PASS:", result["PASS"])
print("FAIL:", result["FAIL"])
print("SKIP:", result["SKIP"])
print("Успешно:", success_percent, "%")