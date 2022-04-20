# While_loop_Lab
#  07 - Min Number

import sys
min_num = sys.maxsize
while True:
    number = input()

    if number == "Stop":
        break
    elif int(number) < min_num:
        min_num = int(number)
print(min_num)
