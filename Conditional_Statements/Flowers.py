# Conditional Statements Advanced - More Exercises
# 03 - Flowers

num_hrizantemi = int(input())
num_roses = int(input())
num_laleta = int(input())
seson = input()
holyday = input()

total_flower = num_hrizantemi + num_roses + num_laleta
cost_hrizantema = 0
cost_roses = 0
cost_laleta = 0
discount = 1

aditional = 1
preparation = 2

if holyday == "Y":
    aditional = 1.15

if seson == "Spring" or seson == "Summer":
    cost_hrizantema = 2
    cost_roses = 4.1
    cost_laleta = 2.5
    if seson == "Spring" and num_laleta > 7:
        discount = 0.95
elif seson == "Autumn" or seson == "Winter":
    cost_hrizantema = 3.75
    cost_roses = 4.5
    cost_laleta = 4.15
    if seson == "Winter" and num_roses >= 10:
        discount = 0.9

total_cost_hrizantemi = num_hrizantemi * cost_hrizantema
total_cost_rozi = num_roses * cost_roses
total_cost_laleta = num_laleta * cost_laleta
total_cost = (total_cost_hrizantemi + total_cost_rozi + total_cost_laleta) * aditional * discount
if total_flower > 20:
    final_cost = (total_cost * 0.8) + preparation

else:
    final_cost = total_cost + preparation

print(f"{final_cost:.2f}")



