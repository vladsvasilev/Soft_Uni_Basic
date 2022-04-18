# Nested Loops - More Exercises
# 03. Lucky Numbers

num = int(input())

for d1 in range(1, 10):
    for d2 in range(1, 10):
        for d3 in range(1, 10):
            for d4 in range(1, 10):
                if d1 + d2 == d3 + d4 and num % (d1 + d2) == 0:
                    print(f"{d1}{d2}{d3}{d4}", end=" ")
