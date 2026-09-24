password = "Python123"
for attempt in range (3):
    user = input()
    if password == user:
        print('Успех')
        break
else:
    print("Доступ заблокирован")