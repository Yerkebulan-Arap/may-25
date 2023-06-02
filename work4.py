user_input = input("Введиту длину в километрах:")

try:
    distance = int(user_input)
except ValueError:
    converter = "Ошибка! Вы ввели не число"
else:
    converter = distance*0.621371

    print("Результат в милях:", converter)

finally:
    print("Работа программы завершена")
    