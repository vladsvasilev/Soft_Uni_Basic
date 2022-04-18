# Nested Loops - Exercise
# 05 - Special Numbers
number = int(input())
for special_n in range(1111, 9999 + 1):
    is_special = True
    special_n = str(special_n)
    for n in special_n:
        n = int(n)
        if n == 0 or number % n != 0:
            is_special = False
            break
    if is_special:
        print(special_n, end=" ")
