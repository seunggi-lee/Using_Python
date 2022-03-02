def solution(seoul):
    answer = [idx for idx, name in enumerate(seoul) if name == "Kim"]
    return "김서방은 " + str(answer[0])+"에 있다"

# def solution(seoul):
#     return "김서방은 {}에 있다".format(seoul.index("Kim"))