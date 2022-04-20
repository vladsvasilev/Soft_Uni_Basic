# While_Loop_Exercise
# 06 - Cake

width = int(input())
length = int(input())

cakes = width * length
is_there_cake = True
command = input()
while command != "STOP":
    current_num_cake = int(command)
    cakes -= current_num_cake
    if cakes < 0:
        is_there_cake = False
        break
    command = input()

if is_there_cake:
    print(f"{cakes} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cakes)} pieces more.")