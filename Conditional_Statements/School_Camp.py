# Conditional Statements Advanced - More Exercises
# 07 - School Camp

season = input()
group_type = input()
num_students = int(input())
nights = int(input())

price = 0
discount = 1
sport = ""

if season == "Winter":
    if group_type == "boys":
        price = 9.6
        sport = "Judo"
    elif group_type == "girls":
        price = 9.6
        sport = "Gymnastics"
    elif group_type == "mixed":
        price = 10
        sport = "Ski"
elif season == 'Spring':
    if group_type == "boys":
        price = 7.2
        sport = "Tennis"
    elif group_type == "girls":
        price = 7.2
        sport = "Athletics"
    elif group_type == "mixed":
        price = 9.5
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        price = 15
        sport = "Football"
    elif group_type == "girls":
        price = 15
        sport = "Volleyball"
    elif group_type == "mixed":
        price = 20
        sport = "Swimming"

if num_students >= 50:
    discount = 0.5
elif 20 <= num_students < 50:
    discount = 0.85
elif 10 <= num_students < 20:
    discount = 0.95

total_price = nights * price * num_students * discount

print(f"{sport} {total_price:.2f} lv.")