from collections import deque

def solution(msg):
    dic = {chr(i + 65): i + 1 for i in range(26)}

    deq = deque(msg)
    answer = []
    num = 27

    w = ""
    while deq:
        w += deq.popleft()
        if w in dic:
            if not deq:
                answer.append(w)
            continue
        elif w not in dic:
            answer.append(w[:-1])
            deq.appendleft(w[-1])
            dic[w] = num
            num += 1
            w = ""

    return [dic[i] for i in answer]