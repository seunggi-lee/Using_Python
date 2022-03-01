import itertools

def solution(numbers):
    answer = []
    group = list(itertools.combinations(numbers, 2))
    for i in group:
        if sum(i) not in answer:
            answer.append(sum(i))

    return sorted(answer)