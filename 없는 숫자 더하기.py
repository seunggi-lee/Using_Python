def solution(numbers):
    answer = 0

    for num in range(10):
        if num not in numbers:
            answer += num
        else:
            pass

    return answer

# 다른 사람의 풀이 (매우 간단 명료하면서도 반박할 수 없는 완벽한 풀이같다.)
# def solution(numbers):
#     return 45 - sum(numbers)