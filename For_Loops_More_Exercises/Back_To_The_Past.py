money = float(input())
years = int(input())
age = 18 - 1 # minus 1 for first year below
money_left = money

for k in range(1800, years + 1):
    age += 1
    if k % 2 == 0:
        money_left -= 12000
    else:
        money_left -= (12000 + (50 * age))

if money_left >= 0:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    needed = abs(money_left)
    print(f"He will need {needed:.2f} dollars to survive.")
