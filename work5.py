user_num_1 = input("Введите 1-e число: ")
user_num_2 = input("Введите 2-e число: ")

try:
    num_1 = int(user_num_1)
    num_2 = int(user_num_2)
    add = num_1 + num_2
    sub = num_1 - num_2
    mul = num_1 * num_2
    div = num_1/num_2
except ValueError:
    print("Вы ввели не число!")
except ZeroDivisionError:
    print('Ошибка! Деление на 0')
    
else:  
    print("Сложение:", add, "Вычетание:", sub, "Умножение:", mul, "Деление:", div)
