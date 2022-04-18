# Nested Loops - More Exercises
# 10. Profit

coin_1_lv = int(input())
coin_2_lv = int(input())
bill_5_lv = int(input())
amount = int(input())

for c1 in range(coin_1_lv + 1):
    for c2 in range(coin_2_lv + 1):
        for b1 in range(bill_5_lv + 1):
            if (c1 * 1) + (c2 * 2) + (b1 * 5) == amount:
                print(f"{c1} * 1 lv. + {c2} * 2 lv. + {b1} * 5 lv. = {amount} lv.")