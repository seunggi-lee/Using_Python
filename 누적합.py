
#1차원 누적합은 sumArr를 구한 후 S(1,4)의 누적합을 구한다고 생각하면 sumArr[5] - sumArr[1]을 계산해주면 구할 수 있다.
#2차원 누적합은 accum함수를 통해 4개의 인자(x1, y1, x2, y2)를 받아서 sumArr에서 sumArr[x2][y2] - sumArr[x1][y2] - sumArr[x2][y1] + sumArr[x1][y1]
#을 계산하면 누적합을 구할 수 있다.


arr = [[1,2,3,4],
       [3,2,1,4],
       [5,4,2,1]]

arr2 = [[1,2,3,4],
        [2,3,4,5],
        [3,4,5,6],
        [4,5,6,7]]

def returnSumArray(arr):

    #행의 합
    sumArr = [[sum(arr[x][:y+1]) for y in range(len(arr[x]))] for x in range(len(arr))]
    # print(sumArr)
    #열의 합 -> 행의 합을 구하면서 산출된 첫 행은 열을 계산해도 변하지 않고 그대로기 때문에 range(1, len(sunArr))를 했음
    for i in range(1, len(sumArr)):
        for j in range(len(sumArr[i])):
            sumArr[i][j] += sumArr[i-1][j]

    print(sumArr)
    return sumArr

def accum(arr, x1, y1, x2, y2):
    sumArr = returnSumArray(arr)

    return sumArr[x2][y2] - sumArr[x1][y2] - sumArr[x2][y1] + sumArr[x1][y1]

print(accum(arr2, 1, 1, 3, 2))