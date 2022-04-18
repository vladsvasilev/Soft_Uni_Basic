# Nested Loops - More Exercises
# 08. Secret Door's Lock

f_num = int(input())
s_num = int(input())
t_num = int(input())

for n1 in range(1, f_num + 1):
    for n2 in range(2, s_num + 1):
        is_prime = True
        for i in range(2, n2):
            if n2 % i == 0:
                is_prime = False
                break
        for n3 in range(1, t_num + 1):
            if n1 % 2 == 0 and n3 % 2 == 0 and is_prime:
                print(f"{n1} {n2} {n3}")
