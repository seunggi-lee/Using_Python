# 시간초과 0 ~ 11 / 12 ~ 15 통과
# import itertools
#
#
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     temp = list(itertools.permutations(numbers, len(numbers)))
#     answer = [int("".join(i)) for i in temp]
#     return str(max(answer))

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int((''.join(numbers))))

print(solution([0,0,0,0]))