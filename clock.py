
# clock.py
import time
import os
from datetime import datetime

target = input("鬧鐘時間 (HH:MM)：")

print("鬧鐘啟動，等待中…")

while True:
    now = datetime.now().strftime("%H:%M")
    if now == target:
        for i in range(5):
            print("⏰ 起床啦！！！")
            os.system("printf '\\a'")
            time.sleep(1)
        break
    time.sleep(1)
