# While-Loop - More Exercises
# 01 - Dishwasher

num_bottles = int(input())

total_detergent = num_bottles * 750
dishes = input()
there_is_detergent = True
count = 1
count_dishes = 0
count_pots = 0

while dishes != "End":
    dishes = int(dishes)
    if dishes > 0:
        if count % 3 != 0:
            count_dishes += dishes
            total_detergent -= dishes * 5
        else:
            count_pots += dishes
            total_detergent -= dishes * 15
        if total_detergent >= 0:
            count += 1
            dishes = input()
        else:
            there_is_detergent = False
            break
    else:
        dishes = input()


diff = abs(total_detergent)
if there_is_detergent:
    print(f"Detergent was enough!")
    print(f"{count_dishes} dishes and {count_pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")
