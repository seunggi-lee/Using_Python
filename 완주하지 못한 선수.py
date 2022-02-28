def solution(participant, completion):
    answer = {}
    for i in participant:
        if i in answer:
            answer[i] += 1
        else:
            answer[i] = 1

    for i in completion:
        if i in answer:
            answer[i] -= 1

    return max(answer, key=lambda x: answer[x])  # max(answer, key=answer.get) 으로도 사용이 가능하다

#효율성이 떨어지는 코드
# def solution(participant, completion):
#     for person in completion:
#         participant.remove(person)
#     return participant[0]

#collection은 객체화 시켜서 뺄셈이 가능
# import collections
#
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]