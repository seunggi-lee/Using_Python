def solution(price, money, count):
    answer = sum([i * price for i in range(1, count + 1)])
    return 0 if answer <= money else answer - money