# Conditional Statements Advanced - More Exercises
# 01 - Match Tickets

budget = float(input())
type_ticket = input()
num_fens = int(input())

cost_transport = 0
cost_tickets = 0
total_cost = 0
left = 0
if 0 < num_fens <= 4:
    cost_transport = budget * 0.75
elif 5 <= num_fens <= 9:
    cost_transport = budget * 0.6
elif 10 <= num_fens <= 24:
    cost_transport = budget * 0.5
elif 25 <= num_fens <= 49:
    cost_transport = budget * 0.4
elif num_fens >= 50:
    cost_transport = budget * 0.25

if type_ticket == "VIP":
    cost_tickets = num_fens * 499.99
elif type_ticket == "Normal":
    cost_tickets = num_fens * 249.99

total_cost = cost_tickets + cost_transport
left = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Yes! You have {left:.2f} leva left.")
else:
    print(f"Not enough money! You need {left:.2f} leva.")