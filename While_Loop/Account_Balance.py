# While_loop_Lab
# 05 - Account Balance

balance = 0

while True:
    number = input()
    if number == "NoMoreMoney":
        break
    elif float(number) < 0:
        print("Invalid operation!")
        break
    balance += float(number)
    print(f"Increase: {float(number):.2f}")

print(f"Total: {balance:.2f}")
