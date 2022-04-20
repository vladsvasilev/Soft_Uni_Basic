# While_Loop_Exercise
# 05 - Coins

sum = float(input())

sum = int(sum * 100)
coins_count = 0

coins_count += sum // 200
sum %= 200
coins_count += sum // 100
sum %= 100
coins_count += sum // 50
sum %= 50
coins_count += sum // 20
sum %= 20
coins_count += sum // 10
sum %= 10
coins_count += sum // 5
sum %= 5
coins_count += sum // 2
sum %= 2
coins_count += sum // 1
sum %= 1

print(coins_count)