num = int(input())

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for n in range(num):
    new_num = int(input())

    if new_num < 200:
        count1 += 1
    elif 200 <= new_num <= 399:
        count2 += 1
    elif 400 <= new_num <= 599:
        count3 += 1
    elif 600 <= new_num <= 799:
        count4 += 1
    elif new_num >= 800:
        count5 += 1

p1 = (count1 / num) * 100
p2 = (count2 / num) * 100
p3 = (count3 / num) * 100
p4 = (count4 / num) * 100
p5 = (count5 / num) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
