# Conditional Statements Advanced - More Exercises
#  08 - Point on Rectangle Border

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

condition1 = False
condition2 = False

if (x == x1 or x == x2) and (y >= y1 and y <= y2):
    condition1 = True
elif (y == y1 or y == y2) and (x >= x1 and x <= x2):
    condition2 = True

if condition1 or condition2:
    print("Border")
else:
    print("Inside / Outside")

