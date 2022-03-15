def solution(n):
    return int(''.join(map(str, sorted(str(int(n)),reverse = True))))