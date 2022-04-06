def solution(number, k):
    answer = []
    number = list(map(int, number))
    for num in number:
        while len(answer) != 0 and answer[-1] < num and k > 0:
            answer.pop()
            k -= 1
        answer.append(num)
    if answer == number:
        answer = answer[:len(answer) - k]

    answer = list(map(str, answer))
    return str("".join(answer))ㅏ