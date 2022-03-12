#제곱근을 이용한 방식
import math
def solution(n):
    answer = 0
    if n <= 1: return 0

    for i in range(2, n + 1):
        result = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                result = False;
                break
        if result:
            answer += 1
    return answer

#에라토스테네스의 체를 이용한 방식
# def solution(n):
#     num = set(range(2, n + 1))
#
#     for i in range(2, n + 1):
#         if i in num:
#             num -= set(range(2 * i, n + 1, i))
#     return len(num)