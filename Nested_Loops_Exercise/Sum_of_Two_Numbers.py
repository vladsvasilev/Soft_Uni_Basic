# Nested Loops - More Exercises
# 09. Sum of Two Numbers

f_num = int(input())
s_num = int(input())
magic_num = int(input())
com_count = 0
end = False
for f in range(f_num, s_num + 1):
    for s in range(f_num, s_num +1):
        com_count += 1
        if f + s == magic_num:
            print(f"Combination N:{com_count} ({f} + {s} = {magic_num})")
            end = True
            break

    if end:
        break

if not end:
    print(f"{com_count} combinations - neither equals {magic_num}")