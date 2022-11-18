def solution(n, k):
    answer = -1
    s = ""
    while True:
        if n < k:
            s += str(n)
            s = s[::-1]
            break
        num, r = divmod(n, k)
        s += str(r)
        n = num
    numList = sorted([int(i) for i in s.split("0") if i != "" and i != '1'])

    isPrime = [True] * len(numList)

    for i in range(len(numList)):
        for j in range(2, int(numList[i] ** 0.5) + 1):
            if numList[i] % j == 0:
                isPrime[i] = False
                break

    return isPrime.count(True)