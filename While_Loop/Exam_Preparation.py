# While_Loop_Exercise
#  02 - Exam Preparation

fail_limit = int(input())

fail_count = 0
sum_grade = 0
problem_count = 0
last_problem = ""
failed = False
problem = input()
while fail_count < fail_limit:

    if problem != "Enough":
        last_problem = problem
        grade = int(input())
        if grade <= 4:
            fail_count += 1
        problem_count += 1
        sum_grade += grade

    else:
        average = sum_grade / problem_count
        print(f"Average score: {average:.2f}")
        print(f"Number of problems: {problem_count}")
        print(f"Last problem: {last_problem}")
        break
    if fail_count < fail_limit:
        problem = input()
    else:
        print(f"You need a break, {fail_count} poor grades.")
        break




