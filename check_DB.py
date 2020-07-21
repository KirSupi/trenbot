# coding=utf-8
import datetime
import time

date = str(datetime.date.today()).split("-")
# count = float(int(date[0]) * 365 * 24 * 60 * 60 + int(date[1]) * 30 * 24 * 60 * 60 + int(date[2]) * 24 * 60 * 60)
# print(count)
# print(time.ctime(count))
print(float(int(date[0]) * 365 * 24 * 60))

# секунды прошли с эпох
seconds = 13722592000
# seconds = 1575721830.711298
local_time = time.ctime(seconds)
print("Местное время:", local_time)