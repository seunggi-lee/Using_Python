# def solution(a, b):
#     answer = b
#     months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
#
#     if a == 1:
#         return days[answer % len(days)-3]
#     else:
#     for i in range(1, a - 1):
#         answer += months[i]
#     return days[answer % len(days)]


def solution(a, b):
    answer = b - 3
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    for i in range(0, a - 1):
        answer += months[i]
    return days[answer % len(days)]