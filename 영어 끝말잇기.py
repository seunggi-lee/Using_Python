from collections import deque

def solution(n, words):
    answer = []
    deq = deque()
    for i in range(len(words)):
        if not deq:
            deq.append(words[i])
            continue
        if words[i] in deq or words[i][0] != deq[-1][-1]:
            answer.append((i % n) + 1)
            answer.append(int(i / n) + 1)
            return answer
        else:
            deq.append(words[i])

    return [0, 0]