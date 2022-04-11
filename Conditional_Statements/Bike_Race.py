# Conditional Statements Advanced - More Exercises
# 02 - Bike Race

num_juniors = int(input())
num_seniors = int(input())
race_type = input()

price_junior = 0
price_senior = 0
total_saved = 0

if race_type == "trail":
    price_junior = 5.50
    price_senior = 7
elif race_type == "cross-country":
    if num_juniors + num_seniors >= 50:
        price_junior = 8 * 0.75
        price_senior = 9.5 * 0.75
    else:
        price_junior = 8
        price_senior = 9.5
elif race_type == "downhill":
    price_junior = 12.25
    price_senior = 13.75
elif race_type == "road":
    price_junior = 20
    price_senior = 21.5

total_saved = ((num_juniors * price_junior) + (num_seniors * price_senior)) * 0.95
print(f"{total_saved:.2f}")
