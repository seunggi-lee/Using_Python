def binarySearch(arr, target):
    arr.sort()
    start = 0
    end = arr.length() - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1


array = [3, 1, 2, 5, 6, 8, 0, 10, 23]

print(binarySearch(array, 6))