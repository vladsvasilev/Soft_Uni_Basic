# For - Loop - More exercises
# 11 - Odd / Even Position
from sys import maxsize
num = int(input())

odd_sum = 0
odd_min = maxsize
odd_max = -maxsize
odd_no_min_dif = False
odd_no_max_dif = False

even_sum = 0
even_min = maxsize
even_max = -maxsize


for n in range(1, num +1):
    new_num = float(input())
    if n % 2 == 0:
        even_sum += new_num
        if new_num < even_min:
            even_min = new_num
        if new_num > even_max:
            even_max = new_num
    else:
        odd_sum += new_num
        if new_num < odd_min:
            odd_min = new_num
        if new_num > odd_max:
            odd_max = new_num

print(f"OddSum={odd_sum:.2f},")

if odd_min == maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")
if even_min == maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == -maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
