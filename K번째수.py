def solution(array, commands):
    answer = []
    for patial_list in commands:
        temp_list = array[patial_list[0] - 1 : patial_list[1]]
        temp_list.sort()
        answer.append(temp_list[patial_list[2] - 1])
    return answer

#최고의 한줄짜리 답
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))