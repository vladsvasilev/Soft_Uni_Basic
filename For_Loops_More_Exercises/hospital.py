# For - Loop - More exercises
# 02 - Hospital

period = int(input())

number_of_doctors = 7
treated_patients = 0
not_treated_patients = 0

for p in range(1, period +1):
    patients = int(input())
    if p % 3 == 0 and not_treated_patients > treated_patients:
        number_of_doctors += 1
    if patients <= number_of_doctors:
        treated_patients += patients
    else:
        treated_patients += number_of_doctors
        not_treated_patients += patients - number_of_doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {not_treated_patients}.")

