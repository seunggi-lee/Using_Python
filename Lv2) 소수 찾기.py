import itertools


def solution(numbers):
    result = set()
    answer = 0

    for i in range(1, len(numbers) + 1):
        per = list(itertools.permutations(numbers, i))
        for j in per:
            result.add(int("".join(j)))

    num_list = list(result)

    for i in num_list:
        isTrue = True
        if i >= 2:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    isTrue = False
                    break
            if isTrue:
                answer += 1
    return answer