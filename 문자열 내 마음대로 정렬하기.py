# def solution(strings, n):
#     strings.sort()
#     return sorted(strings, key=lambda x : x[n])

def solution(strings, n):
    return sorted(sorted(strings), key=lambda x : x[n])