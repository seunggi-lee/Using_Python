from collections import deque


def solution(maps):
    deq = deque()
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    deq.append((0, 0))
    visited[0][0] = True

    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]

    while deq:
        x, y = deq.popleft()  # 0, 0
        if x == n - 1 and y == m - 1:
            return maps[n - 1][m - 1]

        for i in range(4):
            newX = x + mx[i]
            newY = y + my[i]
            if 0 <= newX < n and 0 <= newY < m:
                if maps[newX][newY] == 1 and visited[newX][newY] == False:
                    visited[newX][newY] = True
                    maps[newX][newY] = maps[x][y] + 1
                    deq.append((newX, newY))
                elif maps[newX][newY] == 0 or visited[newX][newY] == True:
                    continue

    return -1
