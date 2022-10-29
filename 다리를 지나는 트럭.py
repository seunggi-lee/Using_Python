from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    complete = []
    n = len(truck_weights)

    bridge = deque(bridge_length * [0])
    truck = deque(truck_weights)
    sumN = 0

    while n != len(complete):
        time += 1
        value = bridge.popleft()
        sumN -= value
        if value != 0:
            complete.append(value)

        if truck and sumN + truck[0] <= weight:
            bridge.append(truck.popleft())
        else:
            bridge.append(0)

        sumN += bridge[-1]

    return time