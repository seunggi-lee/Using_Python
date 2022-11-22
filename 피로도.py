t = 0

def dfs(k, dungeons, depth, visited):
    global t

    if k <= 0:
        return

    if t < depth:
        t = depth

    for i in range(len(dungeons)):
        if dungeons[i][0] <= k and visited[i] == False:
            visited[i] = True
            dfs(k - dungeons[i][1], dungeons, depth + 1, visited)
            visited[i] = False


def solution(k, dungeons):
    visited = [False] * len(dungeons)
    dfs(k, dungeons, 0, visited)

    return t
