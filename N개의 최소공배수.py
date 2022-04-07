def solution(arr):
    answer = []
    arr.sort()

    while len(arr) > 0:
        isEnd = True
        for i in range(arr[-1], arr[-1] * arr[-2] + 1):
            if i % arr[-1] == 0 and i % arr[-2] == 0:
                arr = arr[0:-2]
                answer.append(i)
                break
        for i in sorted(arr, reverse=True):
            if answer[0] % i != 0:
                isEnd = False
                arr.append(answer[0])
                answer = []
                break
            else:
                continue
        if isEnd:
            break

    return answer[0]

# import math
# def solution(arr):
#     answer = arr[0]
#     for n in arr:
#         answer = n * answer // math.gcd(n, answer)
#         print(answer)
#
#     return answer
