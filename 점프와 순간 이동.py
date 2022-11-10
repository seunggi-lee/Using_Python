def solution(n):
    if n == 0:
        return 0
    k = 0

    while True:
        if n == 1:
            k += 1
            n -= 1
            break
        if n % 2 == 1:
            k += 1
            n -= 1
            continue
        elif n % 2 == 0:
            n /= 2

    return k




