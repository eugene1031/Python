#倒數計時器
import time
my_time = int(input("請輸入倒數秒數："))
for x in range(my_time, 0, -1) :
    secs = x % 60
    mins = int(x / 60)
    print(f"{mins:02}:{secs:02}")
    time.sleep(1)
print("Time's up!!!")
