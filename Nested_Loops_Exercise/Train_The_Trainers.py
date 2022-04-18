# Nested Loops - Exercise
# 04 - Train The Trainers

num_people = int(input())
ppt_name = input()
count_ppt = 0
total_assessment = 0
current_assessment = 0

while ppt_name != "Finish":
    temp_assessment = 0
    current_assessment = 0
    count_ppt += 1
    for p in range(num_people):
        assessment = float(input())
        temp_assessment += assessment
        total_assessment += assessment
    current_assessment = temp_assessment / num_people
    print(f"{ppt_name} - {current_assessment:.2f}.")

    ppt_name = input()
final = total_assessment / (count_ppt * num_people)
print(f"Student's final assessment is {final:.2f}.")
