# 답은 맞으나 효율성 1~3 만족 못함
# def solution(people, limit):
#     answer = 0
#     people.sort(reverse=True)
#     temp = 0
#     for i, val in enumerate(people):
#         if val + people[-1] > limit:
#             answer += 1
#             people[i] = limit + 1
#         else:
#             temp = i
#             break
#     for j in range(temp, len(people)):
#         if people[j] <= limit:
#             temp_weight = people[j]
#             people[j] = limit + 1
#             count = j + 1
#             answer += 1
#             while count < len(people):
#                 if temp_weight + people[count] > limit:
#                     count += 1
#                     continue
#                 else:
#                     people[count] = limit + 1
#                     break
#
#     return answer

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    temp = 0
    for i, val in enumerate(people):
        if val + people[-1] > limit:
            answer += 1
            people[i] = limit + 1
        else:
            temp = i
            break

    count = -1
    for j in range(temp, len(people)):
        if people[j] <= limit:
            if people[j] + people[count] <= limit:
                people[count] = limit + 1
                count -= 1
                answer += 1
            else:
                answer += 1
    return answer