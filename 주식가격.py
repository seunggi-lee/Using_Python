def solution(prices):
    answer = []
    for i, j in enumerate(prices):
        count = 0
        for k in range(i + 1, len(prices)):
            if prices[k] >= j:
                count += 1
                continue
            else:
                count += 1
                break
        answer.append(count)
    return answer