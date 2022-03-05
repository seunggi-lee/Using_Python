def solution(a, b):
    answer = sum([i for i in range(a, b + 1)]) if a <= b else sum([i for i in range(b, a + 1)])
    return answer

# def solution(a, b):
#     if a > b: a, b = b, a
#     return sum(range(a, b + 1))
#
#
# def solution(a, b):
#     return (abs(a-b)+1)*(a+b)/2