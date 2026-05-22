dt = '24/07/2015 16:1'
import time
now = time.time()
dt = time.strptime('24/07/2015 16:1', '%d/%m/%Y %H:%M')
dt_epoch = time.mktime(dt)

res = now - dt_epoch
print(res)