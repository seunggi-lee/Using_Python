import time
from collections import deque


def dfs(num):
    if num == m:
        # print(' '.join(result))
        printResult.append(', '.join(result))
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue
        result.append(str(i))
        visited[i] = True
        dfs(num + 1)
        result.pop()
        visited[i] = False

    return


n, m = map(int, input().split())
sT = time.time()
result = []
printResult = []
visited = [False] * (n + 1)

dfs(0)

# for i in printResult:
#   print(i)
# print()
print(len(printResult))
print(time.time() - sT)
# ================================================================================
print()
print()


def dfsDeque(num):
    if num == y:
        # print(' '.join(result))
        printResult.append(', '.join(result))
        return

    for i in range(1, x + 1):
        if visited[i]:
            continue
        result.append(str(i))
        visited[i] = True
        dfsDeque(num + 1)
        result.pop()
        visited[i] = False

    return


x, y = map(int, input().split())
sT = time.time()
result = deque([])
printResult = deque([])
visited = [False] * (x + 1)

dfsDeque(0)

# for i in printResult:
#   print(i)
# print()
print(len(printResult))
print(time.time() - sT)