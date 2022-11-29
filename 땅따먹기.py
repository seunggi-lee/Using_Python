def solution(land):
    answer = 0
    for i in range(1, len(land)):
        maxValue = max(land[i - 1])
        maxIdx = land[i - 1].index(maxValue)
        for j in range(len(land[i])):
            if j != maxIdx:
                land[i][j] += maxValue
            else:
                tempList = sorted(land[i - 1])
                land[i][j] += tempList[-2]
    answer = max(land[len(land) - 1])
    return answer

