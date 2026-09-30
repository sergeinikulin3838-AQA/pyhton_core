with open("file1.bin", "rb") as file:
    data1 = file.read()
with open("file2.bin", "rb") as file:
    data2 = file.read()
with open("file1.bin", "wb") as file:
    file.write(data2)
with open("file2.bin", "wb") as file:
    file.write(data1)