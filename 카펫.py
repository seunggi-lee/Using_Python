def solution(brown, yellow):
    answer = []
    for i in range(brown + yellow, int((brown + yellow) ** 0.5)-1, -1):
        j = (brown + yellow) // i
        if i * j == brown + yellow and i >= j and (i - 2) * (j - 2) == yellow:
            answer.append(i)
            answer.append(j)
    return answer