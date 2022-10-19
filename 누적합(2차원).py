# 참고 : https://yiyj1030.tistory.com/m/489 -> 마지막에 오류가 있음 내 sumArr식이 맞다고 판단
array = [[1, 2, 3, 4],
         [2, 3, 4, 5],
         [3, 4, 5, 6],
         [4, 5, 6, 7]]

array2 = [[0, 0, 2, 4, 1, 7, 5],
          [3, 2, 1, 4, 4, 9, 12],
          [0, -2, 1, 7, 9, 12, 3],
          [4, 5, 6, 2, 1, 0, 0],
          [0, 1, 1, 2, 3, 4, 12]]


def returnSumArr(arr):
    n = len(arr)  # 3
    m = len(arr[0])  # 4

    sumArr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sumArr[i][j] = arr[i - 1][j - 1] + sumArr[i - 1][j] + sumArr[i][j - 1] - sumArr[i - 1][j - 1]

    # print(sumArr)

    return sumArr


def partialSum(arr, x1, y1, x2, y2):
    sumArr = returnSumArr(arr)
    # print(sumArr)

    for i in arr:
        print(i)

    print()
    print()

    for i in sumArr:
        print(i)

    print()

    print(sumArr[x2 + 1][y2 + 1])  #
    print(sumArr[x1][y2 + 1])  #
    print(sumArr[x2 + 1][y1])  #
    print(sumArr[x1][y1])  #

    print()

    return sumArr[x2 + 1][y2 + 1] - sumArr[x1][y2 + 1] - sumArr[x2 + 1][y1] + sumArr[x1][y1]


print(partialSum(array2, 0, 0, 3, 2))


