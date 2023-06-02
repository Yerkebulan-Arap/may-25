number = input("Введите число: ")

try:
    squared_number = int(number) ** 2
except ValueError:
    print("Ошибка! Вы ввели не число")
else:
    print("Квадрат введенного числа: ", squared_number)
finally:
    print("Работа программы завершена")