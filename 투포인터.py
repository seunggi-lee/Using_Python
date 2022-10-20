#리스트가 길어질수록 누적합보다는 슬라이싱이 속도가 더욱 빠르다(누적합 함수를 실행 시 사용되는 반복문 때문이라고 생각됨)
#포맷팅 방식도 알아두기(별도 정리 필요)

import time


def twoPointer1(arr, num):

  sTime = time.time()

  start = end = count = sumNum = 0
  sumArr = partialArray(arr)

  while end < len(arr):
    sumNum = sumArr[end + 1] - sumArr[start]
    # sumNum = sum(arr[start:end + 1])
    # print("Start : ", start, " / End : ", end, " / sumNum : ", sumNum)

    if sumNum >= num:
      start += 1
      if sumNum == num:
        count += 1

    else:
      end += 1

  print("슬라이싱 이용 시간 측정 결과 : %0.100f: " % (time.time() - sTime))
  return count


def twoPointer2(arr, num):

  sTime = time.time()

  start = end = count = sumNum = 0
  # sumArr = partialArray(arr)

  while end < len(arr):
    # sumNum = sumArr[end + 1] - sumArr[start]
    sumNum = sum(arr[start:end + 1])
    # print("Start : ", start, " / End : ", end, " / sumNum : ", sumNum)

    if sumNum >= num:
      start += 1
      if sumNum == num:
        count += 1

    else:
      end += 1

  print("누적합 이용 시간 측정 결과 : %0.100f: " % (time.time() - sTime))
  return count


def partialArray(arr):

  sumArr = [0 for _ in range(len(arr) + 1)]

  for i in range(1, len(arr) + 1):
    sumArr[i] = sumArr[i - 1] + arr[i - 1]

  return sumArr


array = [1, 2, 3, 4, 6, 7, 8, 4, 2, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

print(twoPointer1(array, 5))
print(twoPointer2(array, 5))
