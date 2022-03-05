
#첫 코드
def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    if len(answer) > 0:
        return sorted(answer)
    else: return [-1]

#조금 개선한 두 번째 코드
def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    return sorted(answer) if len(answer) > 0 else [-1]

#사용하면 괜찮을 것 같은 방법
# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]