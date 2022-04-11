# For - Loop - More exercises
# 08 - Equal Pairs
from sys import maxsize
pairs = int(input()) * 2

count_pairs = 0
isFirst = False
isSecond = False
isPair1 = False
isPair2 = False
Eq_pairs = False
f_num = 0
s_num = 0
first_sum = 0
second_sum = 0
delta = 0
max_delta = -maxsize

for i in range(1, pairs + 1):
    new_num = int(input())

    if i % 2 == 0:
        isSecond = True
        s_num = new_num
    else:
        isFirst = True
        f_num = new_num

    if isFirst and isSecond:
        if isPair1:
            isPair2 = True
            second_sum = f_num + s_num
            isFirst = False
            isSecond = False
            count_pairs += 1
        else:
            isPair1 = True
            first_sum = f_num + s_num
            isFirst = False
            isSecond = False
            count_pairs += 1

    if isPair1 and isPair2:
        delta = abs(first_sum - second_sum)
        if max_delta < delta:
            max_delta = delta
        isPair1 = False
        isPair2 = False
    elif isPair1 and i == pairs:
        delta = abs(first_sum - second_sum)
        if max_delta < delta:
            max_delta = delta

if count_pairs == 1:
    print(f"Yes, value={first_sum}")
else:
    if delta == 0:
        print(f"Yes, value={first_sum}")
    else:
        print(f"No, maxdiff={max_delta}")




