def solution(n, lost, reserve):
    students = [1 for x in range(n)]

    for student_num in lost:
        students[student_num - 1] -= 1

    for student_num in reserve:
        students[student_num - 1] += 1

    for idx_i, student in enumerate(students):
        if student == 2:
            if idx_i < n - 1 and students[idx_i + 1] == 0:
                students[idx_i] -= 1
                students[idx_i + 1] += 1

        elif student == 0:
            if idx_i > -1 and idx_i < n - 1 and students[idx_i + 1] > 1:
                students[idx_i] += 1
                students[idx_i + 1] -= 1

    answer = [1 for i in students if i != 0]
    return sum(answer)