import time
import random


WAT = 1
seconds = int(time.time())

real_seconds = seconds % 60

remain = int(seconds / 60)

minutes = remain % 60

remain2 = int(remain/60)

hours = (remain2 % 60) + WAT

days = int(hours/24)



print(days,"-" , hours,":",minutes,":", real_seconds)