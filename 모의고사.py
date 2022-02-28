def solution(answers):
    answer = []
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    student_1 = compareLength(answers, pattern_1)
    student_2 = compareLength(answers, pattern_2)
    student_3 = compareLength(answers, pattern_3)

    result = [0, 0, 0]

    for ans in range(len(answers)):
        if answers[ans] == student_1[ans]:
            result[0] += 1
        if answers[ans] == student_2[ans]:
            result[1] += 1
        if answers[ans] == student_3[ans]:
            result[2] += 1

    max_answer = max(result)

    for i in range(len(result)):
        if result[i] == max_answer:
            answer.append(i + 1)

    return answer


def compareLength(answers, student):
    if len(answers) > len(student):
        num = (len(answers) // len(student)) + 1
        return student * num
    return student