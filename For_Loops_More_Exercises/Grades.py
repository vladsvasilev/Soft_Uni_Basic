# For - Loop - More exercises
# 04 - Grades
number_of_students = int(input())

count_excellent = 0
count_very_good = 0
count_good = 0
count_fail = 0
sum_grades = 0

for s in range(number_of_students):
    grade = float(input())
    sum_grades += grade

    if grade < 3:
        count_fail += 1
    elif 3 <= grade < 4:
        count_good += 1
    elif 4 <= grade < 5:
        count_very_good += 1
    elif grade >= 5:
        count_excellent += 1

top = (count_excellent / number_of_students) * 100
very_good = (count_very_good / number_of_students) * 100
good = (count_good / number_of_students) * 100
fail = (count_fail / number_of_students) * 100
average_grade = sum_grades / number_of_students

print(f"Top students: {top:.2f}%")
print(f"Between 4.00 and 4.99: {very_good:.2f}%")
print(f"Between 3.00 and 3.99: {good:.2f}%")
print(f"Fail: {fail:.2f}%")
print(f"Average: {average_grade:.2f}")