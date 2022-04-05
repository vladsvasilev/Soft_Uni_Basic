exam_hour = int(input())
exam_minute = int(input())
arrival_time = int(input())
arrival_minutes = int(input())

exam_time_in_minutes = (exam_hour * 60) + exam_minute
arrival_time_in_minutes = (arrival_time * 60) + arrival_minutes
min_stat = ""
diff_hours = (abs(exam_time_in_minutes - arrival_time_in_minutes)) // 60
diff_minutes = (abs(exam_time_in_minutes - arrival_time_in_minutes)) % 60
if diff_minutes < 10:
    min_stat = (f"0{diff_minutes}")
else:
    min_stat = diff_minutes

if exam_time_in_minutes < arrival_time_in_minutes:
    if exam_time_in_minutes + 60 > arrival_time_in_minutes:
        print(f'Late')
        print(f"{diff_minutes} minutes after the start")
    else:
        print(f'Late')
        print(f"{diff_hours}:{min_stat} hours after the start")
elif exam_time_in_minutes - 30 <= arrival_time_in_minutes <= exam_time_in_minutes:
    if arrival_time_in_minutes == exam_time_in_minutes:
        print("On time")
    else:
        print("On time")
        print(f"{diff_minutes} minutes before the start")
elif arrival_time_in_minutes < exam_time_in_minutes - 30:
    if arrival_time_in_minutes <= exam_time_in_minutes - 60:
        print(f'Early')
        print(f"{diff_hours}:{min_stat} hours before the start")

    else:
        print(f'Early')
        print(f"{diff_minutes} minutes before the start")

