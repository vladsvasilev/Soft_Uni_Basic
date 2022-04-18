# Nested Loops - More Exercises
# 13. Prime Pairs

first_start = int(input())
second_start = int(input())
first_diff = int(input())
second_diff = int(input())

first_end = first_start + first_diff
second_end = second_start + second_diff


second_prime = True

for f in range(first_start, first_end + 1):
    first_prime = True
    for i in range(2, f):
        if f % i == 0:
            first_prime = False
            break
    for s in range(second_start, second_end + 1):
        second_prime = True
        for j in range(2, s):
            if s % j == 0:
                second_prime = False
                break
        if first_prime and second_prime:
            print(f"{f}{s}")
