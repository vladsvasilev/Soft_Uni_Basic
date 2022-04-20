# While_Loop_Exercise
# 03 - Vacation

needed_money = float(input())
saved_money = float(input())

count_spend_days = 0
count_days = 0
failed = False
while saved_money < needed_money:
    action = input()
    amount = float(input())
    count_days += 1
    if action == "save":
        saved_money += amount
        count_spend_days = 0
    else:
        count_spend_days += 1
        if count_spend_days < 5:
            if saved_money > amount:
                saved_money -= amount
            else:
                saved_money = 0
        else:
            failed = True
            break


if failed:
    print("You can't save the money.")
    print(f"{count_days}")
else:
    print(f"You saved the money for {count_days} days.")
