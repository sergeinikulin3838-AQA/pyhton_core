numbers = []
with open("float_numbers.txt", "r") as file:
    for line in file:
        numbers.append(float(line))
with open("float_numbers.txt", "w") as file:
    for number in numbers:
        file.write(str(number ** 2) + "\n")
print("Все числа возведены в квадрат")