# Nested Loops - Exercise
# 02 - Equal Sums Even Odd Position

first_num = int(input())
second_num = int(input())


for current_num in range(first_num, second_num + 1):
    odd_digits_sum = 0
    even_digits_sum = 0
    n_string = str(current_num)
    for index, value in enumerate(n_string):

        digit_value = int(value)
        if index % 2 == 0:
            odd_digits_sum += digit_value
        else:
            even_digits_sum += digit_value

    if odd_digits_sum == even_digits_sum:
        
        print(n_string, end=" ")
