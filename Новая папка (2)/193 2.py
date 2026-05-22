import time
now = time.time()
res = time.localtime(now)
print(res.tm_hour)