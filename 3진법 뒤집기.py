def solution(n):
    temp = ""

    while True:
        q, r = divmod(n, 3)
        if q == 0:
            temp = temp + str(r)
            break
        else:
            n = q
            temp = temp + str(r)
    return int(str(temp), 3)


# def solution(n):
#     temp = ""
#
#     while n != 0:
#         q, r = divmod(n, 3)
#         temp = temp + str(r)
#         n = q
#     return int(str(temp), 3)