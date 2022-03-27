def solution(n):
    answer = ''
    l = ['4', '1', '2']

    while n > 0:
        q, r = divmod(n, 3)
        answer += l[r]
        if r == 0:
            n = q - 1
        else:
            n = q

    return answer[::-1]