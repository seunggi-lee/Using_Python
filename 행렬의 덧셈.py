def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)
    return answer

# def solution(arr1, arr2):
#     answer = [[a + b for a, b in zip(i, j)] for i, j in zip(arr1, arr2)]
#     return answer