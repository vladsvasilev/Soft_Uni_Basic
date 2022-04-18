# Nested Loops - More Exercises
# 01. Unique PIN Codes

limit1 = int(input())
limit2 = int(input())
limit3 = int(input())
is_prime = True
for d1 in range(1, limit1 + 1):
    for d2 in range(2, limit2 + 1):
        is_prime = True
        for i in range(2, d2):
            if d2 % i == 0:
                is_prime = False
                break
        for d3 in range(1, limit3 +1):
            if d1 % 2 == 0 and is_prime and d3 % 2 == 0:
                print(f"{d1} {d2} {d3}")