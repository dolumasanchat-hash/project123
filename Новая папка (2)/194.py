import time
now = time.time()
res = time.gmtime(now)
print(res.tm_hour)
print(res.tm_min)
# Получаем текущее время в локальном часовом поясе
local_struct = time.localtime()
# Получаем часы и минуты
local_hour = local_struct.tm_hour
local_min = local_struct.tm_min
print(f"Часы по локальному времени: {local_hour}, Минуты: {local_min}")