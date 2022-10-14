array = [8, 4, 2, 6, 5, 3, 1, 10, 9, 3, 1, 5, 4, 7, 8, 34, 3, 4, 1]


def selectionSort(arr):
    if len(arr) < 2:
        return arr

    for i in range(0, len(arr)):
        minIdx = i
        for j in range(i, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr


print("SelectionSort Result : ", selectionSort(array))


def bubleSort(arr):
    if len(arr) < 2:
        return arr

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print("BubleSort Result : ", bubleSort(array))


def insertSort(arr):
    if len(arr) < 2:
        return arr

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


print("InsertSort Result : ", insertSort(array))