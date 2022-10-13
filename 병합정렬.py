array = [8, 4, 2, 1, 7, 3, 10, 9, 0]

def mergeSort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2

    lowArray = mergeSort(array[:mid])
    highArray = mergeSort(array[mid:])

    mergeArray = []
    low = high = 0
    while low < len(lowArray) and high < len(highArray):
        if lowArray[low] < highArray[high]:
            mergeArray.append(lowArray[low])
            low += 1
        else:
            mergeArray.append(highArray[high])
            high += 1
    mergeArray += lowArray[low:]
    mergeArray += highArray[high:]

    return mergeArray

print("Original : ", array)
print("MergeSort : ", mergeSort(array))