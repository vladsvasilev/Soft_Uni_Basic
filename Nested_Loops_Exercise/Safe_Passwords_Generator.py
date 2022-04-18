# Nested Loops - More Exercises
# 07. Safe Passwords Generator

read_a = int(input())
read_b = int(input())
max_pass = int(input())
count = 0
end = False
for n1 in range(35, 56):
    for n2 in range(64, 97):
        for n3 in range(1, read_a + 1):
            for n4 in range(1, read_b + 1):
                print(f"{chr(n1)}{chr(n2)}{n3}{n4}{chr(n2)}{chr(n1)}", end="|")
                count += 1
                if count == max_pass:
                    end = True
                    break
                if n1 >= 55:
                    n1 = 35
                else:
                    n1 += 1
                if n2 >= 96:
                    n2 = 64
                else:
                    n2 += 1
                if n3 == read_a and n4 == read_b:
                    end = True
                    break
            if end:
                break
        if end:
            break
    if end:
        break





