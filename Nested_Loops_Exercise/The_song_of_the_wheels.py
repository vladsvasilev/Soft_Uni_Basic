# Nested Loops - More Exercises
# 12. The song of the wheels

control_num = int(input())
count = 0
password = ""
for n1 in range(1, 10):
    if 4 <= control_num <= 144:
        for n2 in range(1, 10):
            for n3 in range(1, 10):
                for n4 in range(1, 10):
                    if (n1 * n2) + (n3 * n4) == control_num:
                        if n1 < n2 and n3 > n4:
                            count += 1
                            print(f"{n1}{n2}{n3}{n4}", end=" ")
                            if count == 4:
                                password = str(n1) + str(n2) + str(n3) + str(n4)
    else:
        break
print()
if count >= 4:
    print(f"Password: {password}")
else:
    print("No!")
