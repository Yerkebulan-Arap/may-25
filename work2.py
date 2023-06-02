user_input1 = input("Введите 1-е число:")
user_input2 = input("Введите 2-е число:")

try:
    number1 = int(user_input1)
    number2 = int(user_input2)
except ValueError:
    result = "Ошибка! Вы ввели не число"
except OSError:
    result = "Ошибка OC"
else:
    result = (number1+number2)/2
    
print("Результат:", result)
    