# For - Loop - More exercises
# 07 - Football League

capacity = int(input())
num_fens = int(input())

count_A = 0
count_B = 0
count_V = 0
count_G = 0

for f in range(num_fens):
    sector = input()
    if sector == "A":
        count_A += 1
    elif sector == "B":
        count_B += 1
    elif sector == "V":
        count_V += 1
    elif sector == "G":
        count_G += 1

p_A = count_A / num_fens * 100
p_B = count_B / num_fens * 100
p_V = count_V / num_fens * 100
p_G = count_G / num_fens * 100
p_total = num_fens / capacity * 100

print(f"{p_A:.2f}%")
print(f"{p_B:.2f}%")
print(f"{p_V:.2f}%")
print(f"{p_G:.2f}%")
print(f"{p_total:.2f}%")
