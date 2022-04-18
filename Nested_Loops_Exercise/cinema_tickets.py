# Nested Loops - Exercise
# 06 - Cinema Tickets

film = input()

student_count = 0
standard_count = 0
kid_count = 0
count = 0
is_finish = False

while film != "Finish":
    free_place = int(input())
    count = 0
    for place in range(1, free_place + 1):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "Finish":
            is_finish = True
            break
        count += 1
        if ticket_type == "student":
            student_count += 1
        elif ticket_type == "standard":
            standard_count += 1
        elif ticket_type == "kid":
            kid_count += 1
    if is_finish:
        break
    else:
        percentage_film = count / free_place * 100
        print(f"{film} - {percentage_film:.2f}% full.")
        film = input()

total_count = student_count + standard_count + kid_count
p_students = student_count / total_count * 100
p_standard = standard_count / total_count * 100
p_kid = kid_count / total_count * 100

print(f"Total tickets: {total_count}")
print(f"{p_students:.2f}% student tickets.")
print(f"{p_standard:.2f}% standard tickets.")
print(f"{p_kid:.2f}% kids tickets.")