# For - Loop - More exercises
# 06 - Bills

num_months = int(input())

price_water = 20
price_internet = 15

total_electricity = 0
total_water = num_months * price_water
total_internet = num_months * price_internet
total_other = 0
grand_total = 0

for m in range(num_months):
    new_el_price = float(input())
    total_electricity += new_el_price
    total_other += (new_el_price + price_water + price_internet) * 1.2

grand_total = total_electricity + total_water + total_internet + total_other
average = grand_total / num_months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {average:.2f} lv")


