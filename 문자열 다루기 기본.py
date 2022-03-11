# def solution(s):
#     if len(s) == 4 or len(s) == 6:
#         return not [i for i in s if i.isalpha()]
#     else: return False

def solution(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)
