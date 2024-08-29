def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    total_tank, current_tank = 0, 0
    start_station = 0

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]

        if current_tank < 0:
            start_station = i + 1
            current_tank = 0

    return start_station if total_tank >= 0 else -1

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(can_complete_circuit(gas, cost))
