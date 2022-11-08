def solution(n, a, b):
    if a == b and a or b > n:
        return 0

    if a > b:
        a, b = b, a
    answer = 0

    while True:
        answer += 1
        if b == a + 1 and a % 2 == 1:
            break
        if a != 1:
            a = int(a / 2) if a % 2 == 0 else int(a / 2 + 1)
        if b != 1:
            b = int(b / 2) if b % 2 == 0 else int(b / 2 + 1)

    return answer
