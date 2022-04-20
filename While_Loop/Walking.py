# While_Loop_Exercise
# 04 - Walking

target = 10000
total_steps = 0

while total_steps < target:
    command = input()
    if command == "Going home":
        last_steps = int(input())
        total_steps += last_steps
        break

    current_steps = int(command)
    total_steps += current_steps

delta = abs(total_steps - target)
if total_steps > target:
    print(f"Goal reached! Good job!")
    print(f"{delta} steps over the goal!")
else:
    print(f"{delta} more steps to reach goal.")