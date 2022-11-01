def solution(s):
    answer = []
    cnt = 0
    reCnt = 0

    while True:
        reCnt += 1
        tempS = ""
        binaryNum = ""

        for i in range(len(s)):
            if s[i] == "1":
                tempS += "1"
            else:
                cnt += 1

        num = len(tempS)

        while num != 0:
            n, r = divmod(num, 2)
            binaryNum += str(r)
            num = n
            if n == 0:
                break

        s = binaryNum[::-1]
        if s == "1":
            break

    answer.append(reCnt)
    answer.append(cnt)

    return answer
