# While_Loop_Exercise
# 05 - Coins

sum = float(input())

sum = int(sum * 100)
coins_count = 0

while sum > 0:
    if sum // 200 > 0:
        coins_count += sum // 200
        sum %= 200
        continue
    elif sum // 100 > 0:
        coins_count += sum // 100
        sum %= 100
        continue
    elif sum // 50 > 0:
        coins_count += sum // 50
        sum %= 50
        continue
    elif sum // 20 > 0:
        coins_count += sum // 20
        sum %= 20
        continue
    elif sum // 10 > 0:
        coins_count += sum // 10
        sum %= 10
        continue
    elif sum // 5 > 0:
        coins_count += sum // 5
        sum %= 5
        continue
    elif sum // 2 > 0:
        coins_count += sum // 2
        sum %= 2
        continue
    elif sum // 1 > 0:
        coins_count += sum // 1
        sum %= 1
        continue
print(coins_count)
