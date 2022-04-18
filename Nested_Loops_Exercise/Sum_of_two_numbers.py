# Nested Loops - Lab
# 04 - Sum of Two Numbers

interval1 = int(input())
interval2 = int(input())
magic_num = int(input())

comb = 0
founded = False
for i in range(interval1, interval2 + 1):
    for j in range(interval1, interval2 + 1):
        comb += 1
        if i + j == magic_num:
            founded = True
            break
    if founded:
        break

if founded:
    print(f"Combination N:{comb} ({i} + {j} = {magic_num})")
else:
    print(f"{comb} combinations - neither equals {magic_num}")
