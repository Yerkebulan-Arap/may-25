user_input = input("Введите общую сумму продаж: ")

try:
    sale_month = float(user_input)
except ValueError:
    salary = "Вы ввели не число!"

else:
    salary = 250 + (sale_month*10/100)
    
print("Зарплата сотрудника:", salary)