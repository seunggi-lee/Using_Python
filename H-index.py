def solution(citations):
    answer = []
    citations.sort()

    if max(citations) == 0:
        return 0
    n = len(citations)
    maxN = citations[-1]  # 6
    dowN = upN = 0
    for i in range(0, maxN + 1):  # 0~6 / maxN = 6
        h = i + 1  # 0
        count = 0
        for j in range(n):  # 0~4 / n = 5
            temp = citations[j]
            if temp > i:
                dowN = len(citations[:j + 1])
                upN = len(citations[j:])
                if dowN <= h and upN >= h:
                    answer.append(h)
                break

    return answer[-1]