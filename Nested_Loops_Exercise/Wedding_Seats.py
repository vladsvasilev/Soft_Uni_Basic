# Nested Loops - More Exercises
# 06. Wedding Seats

sector = input()
row_num = int(input())
seat_num = int(input())

seat = 0
count = 0


for s in range(65 , ord(sector) + 1):
    for r in range(1, row_num + 1):
        if r % 2 == 0:
            seat += 2
        else:
            seat = seat_num
        ascii_seat = 96
        for s1 in range(1, seat + 1):
            ascii_seat += 1
            print(f"{chr(s)}{r}{chr(ascii_seat)}")
            count += 1
    row_num += 1
print(count)
