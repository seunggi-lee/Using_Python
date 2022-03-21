def solution(x):
    result = 0
    for i in str(x):
        result += int(i)

    return True if x % result == 0 else False

# def solution(x):
#     return True if x % sum([int(i) for i in str(x)]) == 0 else False

    # return x % sum([int(i) for i in str(x)]) == 0

