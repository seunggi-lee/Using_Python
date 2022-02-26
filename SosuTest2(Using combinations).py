import math
from itertools import combinations

def prime(num):

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    cb_result = list(combinations(nums, 3))
    for i in cb_result:
        if prime(sum(i)):
            answer += 1
    return answer

print(solution([1,2,7,6,4]))