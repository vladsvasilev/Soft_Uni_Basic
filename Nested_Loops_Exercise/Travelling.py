# Nested Loops - Lab
# 05 - Travelling

saved_money = 0
ended = False

while True:
    destination = input()

    if destination == "End":
        break
    budget = input()
    if budget == "End":
        break
    budget = float(budget)

    while budget > saved_money:

        new_saving = input()
        if new_saving == "End":
            ended = True
            break
        else:
            new_saving = float(new_saving)
            saved_money += new_saving
    if not ended:
        print(f"Going to {destination}!")
        saved_money = 0
    else:
        break


