user_input = input("Введиту длину квадрата:")

try:
    lenght = int(user_input)
except ValueError:
    print("Ошибка! Вы ввели не число")
else:
    print("Площадь квадрата:", lenght**2)   
finally:
    print("Работа программы завершена")