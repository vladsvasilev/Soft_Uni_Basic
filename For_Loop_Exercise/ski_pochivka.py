days = int(input())
type_of_room = input()
rating = input()

nights = days - 1
cost_per_night = 0
discount = 1

if type_of_room == "room for one person":
    cost_per_night = 18
elif type_of_room == "apartment":
    cost_per_night = 25
    if 0 < days < 10:
        discount = 0.7
    elif 10 <= days <= 15:
        discount = 0.65
    elif days > 15:
        discount = 0.5
elif type_of_room == "president apartment":
    cost_per_night = 35
    if 0 < days < 10:
        discount = 0.9
    elif 10 <= days <= 15:
        discount = 0.85
    elif days > 15:
        discount = 0.8

total_cost = nights * cost_per_night * discount

if rating == "positive":
    total_cost *= 1.25
elif rating == "negative":
    total_cost *= 0.9

print(f"{total_cost:.2f}")
