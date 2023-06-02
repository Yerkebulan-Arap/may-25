user_hours = input("Сколько часов? ")
user_minutes = input("Сколько минут? ")
template = "До конца дня осталось %s часов %s минут"

try:
    hours = int(user_hours)
    minutes = int(user_minutes)
except ValueError:
    message = "Ошибка! Вы ввели не число!"
else:
    remHour = 23 - hours
    remMin = 60 - minutes
    message = template % (remHour, remMin)

print(message)