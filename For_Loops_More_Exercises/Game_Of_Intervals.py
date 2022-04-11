# For - Loop - More exercises
# 05 - Game Of Intervals

number = int(input())

count_0_9 = 0
count_10_19 = 0
count_20_29 = 0
count_30_39 = 0
count_40_50 = 0
count_invalid = 0
total_score = 0

for n in range(number):
    new_num = int(input())
    if 0 <= new_num < 10:
        count_0_9 += 1
        total_score += new_num * 0.2

    elif 10 <= new_num < 20:
        count_10_19 += 1
        total_score += new_num * 0.3
    elif 20 <= new_num < 30:
        count_20_29 += 1
        total_score += new_num * 0.4
    elif 30 <= new_num < 40:
        count_30_39 += 1
        total_score += 50
    elif 40 <= new_num <= 50:
        count_40_50 += 1
        total_score += 100
    elif new_num < 0 or new_num > 50:
        count_invalid += 1
        total_score /= 2

t_0_9 = (count_0_9 / number) * 100
t_10_19 = (count_10_19 / number) * 100
t_20_29 = (count_20_29 / number) * 100
t_30_39 = (count_30_39 / number) * 100
t_40_50 = (count_40_50 / number) * 100
t_invalid = (count_invalid / number) * 100

print(f"{total_score:.2f}")
print(f"From 0 to 9: {t_0_9:.2f}%")
print(f"From 10 to 19: {t_10_19:.2f}%")
print(f"From 20 to 29: {t_20_29:.2f}%")
print(f"From 30 to 39: {t_30_39:.2f}%")
print(f"From 40 to 50: {t_40_50:.2f}%")
print(f"Invalid numbers: {t_invalid:.2f}%")
