import datetime
# Получаем текущую дату
today = datetime.date.today()
# Форматируем строку в нужном виде
formatted_date = today.strftime("%d.%m.%Y")
# Выводим результат
print(formatted_date)