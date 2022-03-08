# def solution(s):
#     answer = True
#     str = s.lower()
#     count_1 = str.count("p")
#     count_2 = str.count("y")
#     if count_1 == count_2:
#         return True
#
#     return False

def solution(s):
    return s.lower().count('p') == s.lower().count('y')
