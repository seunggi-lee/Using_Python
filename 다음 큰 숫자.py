def solution(n):
    answer = 0

    oneNum = binaryTransform(n).count("1")

    while True:
        n += 1
        otherNum = binaryTransform(n).count("1")
        if otherNum == oneNum:
            return n


def binaryTransform(num):
    temp = ""
    while num != 0:
        n, r = divmod(num, 2)
        temp += str(r)
        num = n
    return temp[::-1]