def solution(priorities, location):
    answer = 0
    count = 0
    while len(priorities) > 0:
        if priorities[0] == max(priorities):
            priorities.pop(0)
            count += 1
            if location == 0:
                answer = count
                break
            else:
                location -= 1
        else:
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1

    return answer