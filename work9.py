user_input = input("Введите пятизначное число: ")

try:
    five_dig = int(user_input)
    rem_div = five_dig%10
    int_div = five_dig//10
except ValueError as ex:
    result = "Ошибка! вы ввели не пятизначное число"

else:
    result = (rem_div*10**4)+int_div
    
print("Результат:", result)