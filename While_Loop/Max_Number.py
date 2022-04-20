# While_loop_Lab
# 06 - Max Number
import sys
max_num = -sys.maxsize
while True:
    number = input()

    if number == "Stop":
        break
    elif int(number) > max_num:
        max_num = int(number)
print(max_num)