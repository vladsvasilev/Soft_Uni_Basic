sites = int(input())
salary = int(input())
deduct = 0
for n in range(sites):
    site_name = input()

    if site_name == "Facebook":
        deduct += 150
    elif site_name == "Instagram":
        deduct += 100
    elif site_name == "Reddit":
        deduct += 50

left = salary - deduct
if salary > deduct:
    print(left)
else:
    print("You have lost your salary.")
