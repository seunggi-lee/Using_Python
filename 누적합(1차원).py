array = [3, 4, 2, 1, 5, 6, 2, 1]


def returnPartialSumArray(arr, x, y):
    n = len(arr)
    sumArr = [0 for _ in range(len(arr) + 1)]

    for i in range(1, n + 1):
        sumArr[i] = arr[i - 1] + sumArr[i - 1]

    print(sumArr)
    print()

    return sumArr[y + 1] - sumArr[x]


print(returnPartialSumArray(array, 2, 7))