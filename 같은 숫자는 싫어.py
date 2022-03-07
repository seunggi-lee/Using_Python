def solution(arr):
    answer = []
    for idx, value in enumerate(arr):
        if idx == 0:
            answer.append(value)
        else:
            if value == arr[idx - 1]:
                continue
            else:
                answer.append(value)

    return answer

# def solution(arr):
#     answer = []
#     for value in arr:
#         if answer[-1:] == [value]:
#             continue
#         answer.append(value)
#     return answer

# def solution(arr):
#     answer = []
#     for value in arr:
#         if len(answer) != 0 and answer[len(answer) - 1] == value:
#             continue
#         answer.append(value)
#     return answer