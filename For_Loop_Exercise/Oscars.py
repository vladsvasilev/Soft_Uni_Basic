act_name = input()
score_academy = float(input())
num_evaluators = int(input())

count = 0
total_score = score_academy
name_length = 0

for n in range(num_evaluators):
    count += 1
    evaluater_name = input()
    new_score = float(input())
    name_length = len(evaluater_name)
    total_score += ((name_length * new_score) / 2)
    if total_score > 1250.5:
        break

if total_score < 1250.5:
    diff = 1250.5 - total_score
    print(f"Sorry, {act_name} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {act_name} got a nominee for leading role with {total_score:.1f}!")



