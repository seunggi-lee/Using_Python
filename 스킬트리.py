def solution(skill, skill_trees):
    answer = 0

    for i in range(len(skill_trees)):
        temp = ""
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                temp += skill_trees[i][j]
        if temp == skill[:len(temp)]:
            answer += 1

    return answer