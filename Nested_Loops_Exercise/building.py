# Nested Loops - Lab
# 06 - Building

floors = int(input())
rooms = int(input())

for f in range(floors, 0, -1):
    for r in range(rooms):
        room_num = f * 10 + r
        if f == floors:

            print(f"L{room_num}", end=" ")
        elif f % 2 == 0:
            print(f"O{room_num}", end=" ")
        else:
            print(f"A{room_num}", end=" ")
    print()

