# Conditional Statements Advanced - More Exercises
# 10 - Multiply by 2

i = float(input())
if i < 0:
    print("Negative number!")
while i >= 0:

    i *= 2
    print(F"Result: {i:.2f}")
    i = float(input())
    if i < 0:
        print("Negative number!")

