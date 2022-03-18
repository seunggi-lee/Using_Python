def solution(n):
    return [int(str(n)[len(str(n)) - i - 1]) for i in range(len(str(n)))]