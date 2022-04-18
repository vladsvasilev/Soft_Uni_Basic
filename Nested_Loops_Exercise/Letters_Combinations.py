# Nested Loops - More Exercises
# 02. Letters Combinations

first = input()
second = input()
without = input()
count = 0
for l1 in range(ord(first), ord(second) + 1):
    for l2 in range(ord(first), ord(second) + 1):
        for l3 in range(ord(first), ord(second) + 1):
            if l1 != ord(without) and l2 != ord(without) and l3 != ord(without):
                count += 1

                print(f"{chr(l1)}{chr(l2)}{chr(l3)}", end=" ")
print(count, end=" ")