# While-Loop - More Exercises
#  05 - Average Number

num = int(input())
sum = 0
for n in range(num):
    new_num = int(input())
    sum += new_num
avg = sum / num
print(f"{avg:.2f}")
