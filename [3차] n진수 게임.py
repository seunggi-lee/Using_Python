def transN(num, n):
    s = ""
    while True:
        if num < n:
            if 10 <= num <= 15:
                num = chr(num + 55)
            s += str(num)
            break
        q, r = divmod(num, n)
        if 10 <= r <= 15:
            r = chr(r + 55)
        s += str(r)
        num = q
    return s[::-1]


def solution(n, t, m, p):
    answer = ""
    num = 0
    cnt = 1
    while True:
        temp = transN(num, n)
        for i in temp:
            if cnt == p:
                answer += i
                if len(answer) == t:
                    return answer
                if m == cnt:
                    cnt = 1
                else:
                    cnt += 1
            else:
                if m == cnt:
                    cnt = 1
                    continue
                cnt += 1

        num += 1
    return answer