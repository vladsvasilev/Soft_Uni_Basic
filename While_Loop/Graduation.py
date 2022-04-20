# While_loop_Lab
# 08 - Graduation

name = input()

grade = 0
sum_all_years = 0

while grade < 12:
    new_grade = float(input())
    grade += 1
    if new_grade >= 4:
        sum_all_years += new_grade

    elif new_grade < 4:
        new_grade_1 = float(input())
        if new_grade_1 < 4:
            print(F"{name} has been excluded at {grade} grade")
            break
        else:
            sum_all_years += new_grade_1
if grade == 12:
    average = sum_all_years / grade
    print(f"{name} graduated. Average grade: {average:.2f}")