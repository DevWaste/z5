# Ввод строки пользователем
input_string = input("Введите строку: ")

# Преобразование всех подряд идущих пробелов в один
# Сначала split() разделяет строку, удаляя лишние пробелы, затем ' '.join() объединяет элементы с одним пробелом между ними
output_string = ' '.join(input_string.split())

# Вывод результата
print(output_string)
