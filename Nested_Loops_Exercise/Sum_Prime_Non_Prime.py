# Nested Loops - Exercise
# 03 - Sum Prime Non Prime

sum_of_prime = 0
sum_of_non_prime = 0
command = input()

while command != 'stop':
    number = int(command)
    if number < 0:
        print("Number is negative.")
    else:
        number_is_prime = True
        for n in range(2, number):
            if number % n == 0:
                number_is_prime = False
                break
        if number_is_prime:
            sum_of_prime += number
        else:
            sum_of_non_prime += number
    command = input()

print(f"Sum of all prime numbers is: {sum_of_prime}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime}")
