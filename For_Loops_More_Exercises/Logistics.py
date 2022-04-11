# For - Loop - More exercises
# 03 - Logistic

numbers_of_loads = int(input())

total_load = 0
cost = 0
total_cost = 0
bus_loads = 0
truck_loads = 0
train_loads = 0

for l in range(numbers_of_loads):
    load_info = int(input())
    total_load += load_info

    if 0 < load_info <= 3:
        bus_loads += load_info
        cost = load_info * 200
    elif 3 < load_info <= 11:
        truck_loads += load_info
        cost = load_info * 175
    elif load_info > 11:
        train_loads += load_info
        cost = load_info * 120
    total_cost += cost

average_tones = total_cost / total_load
average_bus = (bus_loads / total_load) * 100
average_truck = (truck_loads / total_load) * 100
average_train = (train_loads / total_load) * 100

print(f"{average_tones:.2f}")
print(f"{average_bus:.2f}%")
print(f"{average_truck:.2f}%")
print(f"{average_train:.2f}%")


