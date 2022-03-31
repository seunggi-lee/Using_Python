def solution(n):
    count = 0
    a, b = 0, 1
    while count < n:
        count += 1
        a, b = b, a + b

    return a % 1234567