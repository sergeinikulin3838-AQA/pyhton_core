
with open("numbers.txt", "r") as file:
    numbers = file.readlines()
with open("even.txt", "w") as even_file:
    with open("odd.txt", "w") as odd_file:
        for line in numbers:
            number = int(line)
            if number % 2 == 0:
                even_file.write(str(number) + "\n")
            else:
                odd_file.write(str(number) + "\n")
print("Числа распределены по файлам")