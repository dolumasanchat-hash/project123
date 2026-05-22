dt1 = '13/10/2018 22:15:45'
dt2 = '15/11/2018 09:47:16'
import datetime
start_time = datetime.datetime.strptime('13/10/2018 22:15:45', '%d/%m/%Y %H:%M:%S')
end_time = datetime.datetime.strptime('15/11/2018 09:47:16', '%d/%m/%Y %H:%M:%S')
res = end_time - start_time
print(res)