numbers = []
with open("numbers.txt", "r") as file:
    for line in file:
        numbers.append(int(line))
if len(numbers) < 3:
    print("Ошибка: в файле меньше 3 чисел")
else:
    print("Первый:", numbers[0])
    print("Второй:", numbers[1])
    print("Предпоследний:", numbers[-2])
    print("Последний:", numbers[-1])