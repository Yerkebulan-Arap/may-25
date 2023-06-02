user_input = input("Введите трехзначное число: ")

try:
    three_digit = int(user_input)
    int_div = three_digit//10
    rem_div = int_div%10
except ValueError:
    print("Вы ввели не трехзначное число!")

else:
    print("Второя цифра:", rem_div)

finally:
    print("Все правильно")