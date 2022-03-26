# def solution(progresses, speeds):
#     answer = []
#     day_count = []
#
#     for i, j in zip(progresses, speeds):
#         if (100 - i) / j == (100 - i) // j:
#             day_count.append((100 - i) // j)
#         else:
#             day_count.append((100 - i) // j + 1)
#
#     standard_num = 0
#     count = 1
#     for i in range(1, len(day_count)):
#         if day_count[standard_num] >= day_count[i]:
#             count += 1
#             if i == len(day_count) - 1:
#                 answer.append(count)
#                 break
#         else:
#             answer.append(count)
#             standard_num = i
#             count = 1
#             if standard_num == len(day_count) - 1:
#                 answer.append(count)
#                 break
#
#     return answer

import math


def solution(progresses, speeds):
    answer = []

    day_count = [math.ceil((100 - i) / j) for i, j in zip(progresses, speeds)]

    standard_num = 0
    count = 1
    for i in range(1, len(day_count)):
        if day_count[standard_num] >= day_count[i]:
            count += 1
            if i == len(day_count) - 1:
                answer.append(count)
                break
        else:
            answer.append(count)
            standard_num = i
            count = 1
            if standard_num == len(day_count) - 1:
                answer.append(count)
                break

    return answer
