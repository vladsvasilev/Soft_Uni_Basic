from math import floor
num_tournaments = int(input())
initial_score = int(input())

total_wins = 0
total_score = initial_score

for n in range(num_tournaments):
    tournament_status = input()

    if tournament_status == "W":
        total_score += 2000
        total_wins += 1
    elif tournament_status == "F":
        total_score += 1200
    elif tournament_status == "SF":
        total_score += 720
average_points = floor((total_score - initial_score) / num_tournaments)
percentage = total_wins / num_tournaments * 100

print(f"Final points: {total_score}")
print(f"Average points: {average_points}")
print(f"{percentage:.2f}%")


