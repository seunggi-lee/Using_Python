def solution(num):
    count = 0
    while True:
        if num == 1:
            return count
        count += 1
        num = num * 3 + 1 if num % 2 else num / 2

        if count >= 500:
            return -1