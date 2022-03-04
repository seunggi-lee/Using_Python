def solution(a, b):
    answer = 0
    for a_, b_ in zip(a, b):
        answer += (a_ * b_)
    return answer