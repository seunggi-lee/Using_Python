# 효율성 초과된 코드
# def solution(phone_book):
#     answer = True
#     phone_book.sort(key=len)
#
#     for idx, val in enumerate(phone_book):
#         if answer == False:
#             break
#         for i in range(idx + 1, len(phone_book)):
#             if val == phone_book[i][0: len(val)]:
#                 answer = False
#                 break
#         if answer == False:
#             break
#     return answer


def solution(phone_book):
    answer = True
    phone_book.sort()

    for idx, val in enumerate(phone_book):
        if idx != len(phone_book) - 1:
            if val == phone_book[idx + 1][0: len(val)]:
                answer = False
                break
    return answer

solution(["119", "97674223", "1195524421"])