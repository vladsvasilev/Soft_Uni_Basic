# While-Loop - More Exercises
# 02 - Report system

expected_money = int(input())
new_amount = input()


cash_only = False
expected_payment_method = "cash"
card_only = False
count = 1
collected = 0
is_enough = False
cash_collected = 0
count_cash = 0
card_collected = 0
count_card = 0

while new_amount != "End":
    new_amount = int(new_amount)


    if count % 2 == 0:
        expected_payment_method = "card"
    else:
        expected_payment_method = "cash"

    if new_amount > 100:
        card_only = True
    elif new_amount < 10:
        cash_only = True
    elif 10 <= new_amount <= 100:
        cash_only = True
        card_only = True

    if card_only and expected_payment_method == "card":
        card_collected += new_amount
        count_card += 1
        print("Product sold!")

    elif cash_only and expected_payment_method == "cash":
        cash_collected += new_amount
        count_cash += 1
        print("Product sold!")

    else:
        print("Error in transaction!")

    collected = cash_collected + card_collected

    if collected < expected_money:
        new_amount = input()
        count += 1
        card_only = False
        cash_only = False
    else:
        is_enough = True
        break

if cash_collected > 0:
    average_cash = cash_collected / count_cash
else:
    average_cash = 0
if card_collected > 0:
    average_card = card_collected / count_card
else:
    average_card = 0


if is_enough and new_amount != "End":
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")
else:
    print(f"Failed to collect required money for charity.")
