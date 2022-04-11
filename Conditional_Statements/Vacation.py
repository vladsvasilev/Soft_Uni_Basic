# Conditional Statements Advanced - More Exercises
# 05 - Vacation

budget = float(input())
seson = input()

location = ""
type_accommodation = ""
cost = budget

if budget <= 1000:
    type_accommodation = "Camp"
    if seson == "Summer":
        location = "Alaska"
        cost *= 0.65
    elif seson == "Winter":
        location = "Morocco"
        cost *= 0.45

elif 1000 < budget <= 3000:
    type_accommodation = "Hut"
    if seson == "Summer":
        location = "Alaska"
        cost *= 0.80
    elif seson == "Winter":
        location = "Morocco"
        cost *= 0.60
elif budget > 3000:
    type_accommodation = "Hotel"
    if seson == "Summer":
        location = "Alaska"
        cost *= 0.9
    elif seson == "Winter":
        location = "Morocco"
        cost *= 0.9

print(f"{location} - {type_accommodation} - {cost:.2f}")
