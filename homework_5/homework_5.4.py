with open("first.bin", "rb") as file:
    first_data = file.read()
with open("second.bin", "rb") as file:
    second_data = file.read()
with open("first.bin", "wb") as file:
    file.write(second_data)
with open("second.bin", "wb") as file:
    file.write(first_data)
print("Содержимое файлов поменялось местами")
