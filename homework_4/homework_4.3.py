with open("numbers.txt", "r") as file:
    numbers = list(map(float, file.read().split()))
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2
with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + " ")