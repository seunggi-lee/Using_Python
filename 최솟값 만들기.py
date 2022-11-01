import heapq


def solution(A, B):
    answer = []
    heapq.heapify(A)
    heapq.heapify(B)

    tempB = []
    heapq.heapify(tempB)

    for i in range(len(B)):
        heapq.heappush(tempB, -1 * heapq.heappop(B))
    print(tempB)

    for i in range(len(A)):
        answer.append(heapq.heappop(A) * (-1 * heapq.heappop(tempB)))

    return sum(answer)