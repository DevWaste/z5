input_string = input("Введите строку: ")

# Проверка, является ли строка палиндромом
if input_string == input_string[::-1]:  # Сравниваем строку с ее версией в обратном порядке
    print("yes")
else:
    print("no")
