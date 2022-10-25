from collections import deque

def solution(s):
    answer = True
    deq = deque([])

    if s[0] == ')' or s[len(s) - 1] == '(':
        return False

    for i in s:
        if i == '(':
            deq.append(i)
        elif i == ')' and deq:
            deq.pop()

    if deq:
        answer = False
    return answer