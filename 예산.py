def solution(d, budget):
    d.sort()
    answer = []
    for i in d:
        if sum(answer) + i <= budget:
            answer.append(i)
    return len(answer)