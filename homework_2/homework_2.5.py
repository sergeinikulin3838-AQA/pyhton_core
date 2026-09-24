tests_count = int(input("Введите количество автотестов "))

pass_count = 0
fail_count = 0
skip_count = 0

for test in range(tests_count):
    status = input("Введите результат теста: ")

    if status == "PASS":
        pass_count = pass_count + 1
    elif status == "FAIL":
        fail_count = fail_count + 1
    elif status == "SKIP":
        skip_count = skip_count + 1
    else:
        continue

print("PASS:", pass_count)
print("FAIL:", fail_count)
print("SKIP:", skip_count)

if fail_count > 0:
    print("Есть упавшие тесты")
else:
    print("Выполненные тесты успешно пройдены")