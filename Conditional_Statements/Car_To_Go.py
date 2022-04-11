# Conditional Statements Advanced - More Exercises
# 04 - Car To Go

budget = float(input())
seson = input()

class_vehicle = ""
type_vehicle = ""
price = budget

if budget <= 100:
    class_vehicle = "Economy class"
    if seson == "Summer":
        type_vehicle = "Cabrio"
        price *= 0.35
    elif seson == "Winter":
        type_vehicle = "Jeep"
        price *= 0.65
elif 100 < budget <= 500:
    class_vehicle = "Compact class"
    if seson == "Summer":
        type_vehicle = "Cabrio"
        price *= 0.45
    elif seson == "Winter":
        type_vehicle = "Jeep"
        price *= 0.80
elif budget > 500:
    class_vehicle = "Luxury class"
    type_vehicle = "Jeep"
    price *= 0.9

print(class_vehicle)
print(f"{type_vehicle} - {price:.2f}")
