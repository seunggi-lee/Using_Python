from queue import Queue


def BFS(graph, node, visited):
    que = Queue()
    que.put(node)
    visited[node] = True

    checkL = []

    while que.qsize() != 0:
        v = que.get()
        checkL.append(v)

        for i in graph[v]:
            if visited[i] == False:
                que.put(i)
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

visited = [False] * 9

for i in BFS(graph, 1, visited):
    print(i, end=' ')

print()

visited2 = [False] * 9

for i in BFS(graph, 8, visited2):
    print(i, end=' ')