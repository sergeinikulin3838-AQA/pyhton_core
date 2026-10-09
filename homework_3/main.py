import test_data
count = int(input("Введите количество тестовых пользователей: "))
users = []
for i in range(count):
    user = test_data.generate_user()
    users.append(user)
active_count = 0
blocked_count = 0
inactive_count = 0
for user in users:
    print(user)
    if user["status"] == "ACTIVE":
        active_count += 1
    elif user["status"] == "BLOCKED":
        blocked_count += 1
    elif user["status"] == "INACTIVE":
        inactive_count += 1
print("ACTIVE:", active_count)
print("BLOCKED:", blocked_count)
print("INACTIVE:", inactive_count)