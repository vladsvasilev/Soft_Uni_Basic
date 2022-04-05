import sys
num = int(input())

max_num = -sys.maxsize
sum_num = 0

for n in range(num):
    new_number = int(input())

    if new_number > max_num:
        max_num = new_number

    sum_num += new_number

if max_num == sum_num - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - (sum_num - max_num))
    print("No")
    print(f"Diff = {diff}")
