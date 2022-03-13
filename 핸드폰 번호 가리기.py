def solution(phone_number):
    answer = ''
    length = len(phone_number) - 5
    for i in range(len(phone_number)):
        if i <= length:
            answer = answer + '*'
        else:
            answer += phone_number[i]

    return answer

# def solution(phone_number):
#     return '*' * (len(phone_number) - 4) + phone_number[-4 : ]