#a * x + b = 0
user_input_1 = input("Введите а: ")
user_input_2 = input("Введите b: ")

try:
    a = int(user_input_1)
    b = int(user_input_2) 
    x = -b/a
except ValueError:
    print("Вы ввели не число!")
except ZeroDivisionError:
    print('Ошибка! Деление на 0')
    
else:  
    print("Результат значении х:", x)
