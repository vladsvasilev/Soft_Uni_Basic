number_of_groups = int(input())

group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0
total_members = 0

for n in range(number_of_groups):
    members_in_group = int(input())
    total_members += members_in_group
    if members_in_group <= 5:
        group_1 += members_in_group
    elif 6 <= members_in_group <= 12:
        group_2 += members_in_group
    elif 13 <= members_in_group <= 25:
        group_3 += members_in_group
    elif 26 <= members_in_group <= 40:
        group_4 += members_in_group
    elif members_in_group >= 41:
        group_5 += members_in_group
p1 = group_1 / total_members * 100
p2 = group_2 / total_members * 100
p3 = group_3 / total_members * 100
p4 = group_4 / total_members * 100
p5 = group_5 / total_members * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

