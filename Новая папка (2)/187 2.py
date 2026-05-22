from datetime import datetime
# Даты в формате: день-месяц-год часы:минуты:секунды
dt1 = '01-12-2025 16:07:05'
dt2 = '31-12-2025 10:32:45'
# Формат даты
date_format = '%d-%m-%Y %H:%M:%S'
# Преобразуем строки в объекты datetime
datetime1 = datetime.strptime(dt1, date_format)
datetime2 = datetime.strptime(dt2, date_format)
# Вычисляем разницу
time_difference = datetime2 - datetime1
print(f'Прошло времени: {time_difference}')