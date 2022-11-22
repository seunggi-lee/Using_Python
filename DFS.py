from collections import deque


def DFS(graph, node):
    deq = deque()
    visited = [False] * 9
    deq.append(node)
    visited[node] = True

    checkL = []

    while deq:
        v = deq.pop()

        checkL.append(v)

        for i in graph[v]:
            if visited[i] == False:
                deq.append(i)
                visited[i] = True

    return checkL


graph = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

for i in DFS(graph, 1):
    print(i, end=' ')

print()

for i in DFS(graph, 8):
    print(i, end=' ')