from collections import deque


def solution(s):
    deq = deque()

    for i in s:
        if not deq:
            deq.append(i)
            continue
        if deq[-1] == i:
            deq.pop()
        else:
            deq.append(i)
    return 1 if len(deq) == 0 else 0

#     S = deque(list(s))

#     while S:
#         val = S.popleft()
#         if not deq:
#             deq.append(val)
#             continue
#         if deq[-1] == val:
#             deq.pop()
#         else:
#             deq.append(val)
#     return 1 if len(deq) == 0 else 0