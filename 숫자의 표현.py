def solution(n):
    target = n

    arr = [i for i in range(1, n + 1)]
    s = e = cnt = 0

    while e < len(arr):
        sumN = sum(arr[s:e + 1])

        if sumN >= target:
            s += 1
            if sumN == target:
                cnt += 1
        else:
            e += 1

    return cnt