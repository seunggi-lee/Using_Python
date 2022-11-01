def solution(s):
    answer = ""
    temp = s.lower()
    print(temp)
    for i in range(len(temp)):
        if i == 0:
            answer += temp[i].upper()
        else:
            if temp[i] != " " and temp[i - 1] == " ":
                answer += temp[i].upper()
            else:
                answer += temp[i]

    return answer