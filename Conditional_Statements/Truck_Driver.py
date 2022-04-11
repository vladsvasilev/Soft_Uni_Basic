# Conditional Statements Advanced - More Exercises
# 06 - Truck Driver

season = input()
km_month = float(input())

total_km_season = km_month * 4
price_km = 0
total_price_season = total_km_season * price_km * 0.9

if km_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_km = 0.75
    elif season == "Summer":
        price_km = 0.9
    elif season == "Winter":
        price_km = 1.05
elif 5000 < km_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_km = 0.95
    elif season == "Summer":
        price_km = 1.1
    elif season == "Winter":
        price_km = 1.25
elif 10000 < km_month <= 20000:
    price_km = 1.45
total_price_season = total_km_season * price_km * 0.9
print(f"{total_price_season:.2f}")
