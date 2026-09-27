number = 37
attempts  = 0
a = 0
while a != 37:
    attempts = attempts + 1
    a = int(input())
    if a < 37:
        print("Число больше ")
    elif a > 37:
        print("Число меньше")
    else:
        print("Угадал", "Количество попыток ", attempts)