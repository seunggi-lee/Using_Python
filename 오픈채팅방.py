def solution(record):
    answer = []
    id_dic = {}
    command = [i.split() for i in record]

    for i in command:
        if i[0] == "Enter" or i[0] == "Change":
            id_dic[i[1]] = i[2]

    for i in command:
        if i[0] == "Enter":
            answer.append(id_dic[i[1]] + "님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(id_dic[i[1]] + "님이 나갔습니다.")

    return answer