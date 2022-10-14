#파이썬 난수 발생시키는 방법
#import random
#num = random.randrange(0,len(array) - 1)

import random
array = [8,4,3,2,6,5,10,9] # 현재 같은 숫자가 있으면 정렬이 안됨

def QuickSort(arr):
  if len(arr) < 2:
    return arr

  # pNum = random.randrange(0, len(arr))
  pivot = arr[len(arr) // 2]

  frontArr, middleArr, backArr = [], [], []

  for i in range(0, len(arr)):
    if arr[i] < pivot:
      frontArr.append(arr[i])
    elif arr[i] > pivot:
      backArr.append(arr[i])
    else:
      middleArr.append(arr[i])
  return QuickSort(frontArr) + QuickSort(middleArr) + QuickSort(backArr)

print("QuickSort : ", QuickSort(array))