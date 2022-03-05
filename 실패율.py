# def solution(N, stages): #시간 매우 오래 걸림
#     answer = []
#     prop = {}
#     user_num = len(stages)
#     stage_count = []
#     for idx in range(1, N + 1):
#         num = stages.count(idx)
#         prop[idx] = num / user_num
#         user_num -= num
#
#     sorted_prop = sorted(prop.items(), key=lambda x: x[1], reverse=True)
#     for value in sorted_prop:
#         answer.append(int(value[0]))
#     return answer

def solution(N, stages):
    answer = []
    prop = {}
    user_num = len(stages)
    stage_count = [0 for i in range(N)]

    for i, stage in enumerate(stages):
        if stage > N:
            continue
        else:
            stage_count[stage - 1] += 1

    for idx in range(len(stage_count)):
        if user_num == 0:
            prop[idx + 1] = 0
            continue
        if idx < N:
            prop[idx + 1] = stage_count[idx] / user_num
            user_num -= stage_count[idx]

    sorted_prop = sorted(prop.items(), key=lambda x: x[1], reverse=True)
    for value in sorted_prop:
        answer.append(int(value[0]))
    return answer