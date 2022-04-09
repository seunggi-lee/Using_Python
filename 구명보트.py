def solution(people, limit):
    answer = 0
    temp = 0
    min_weight = 40
    for idx, val in enumerate(people):
        temp_weight = 0
        if idx != len(people) - 1:
            if val + min_weight >= limit:
                answer += 1
                people[idx] = limit + 1
                continue

            elif people[idx] > limit:
                continue

            else:
                temp_weight = val
                for j in range(idx + 1, len(people)):
                    if temp_weight + people[j] <= limit:
                        temp_weight += people[j]
                        people[j] = limit + 1
                        if temp_weight + min_weight >= limit:
                            answer += 1
                            break
                        else:
                            continue
                    else:
                        continue
        else:
            if val > limit:
                break
            else:
                answer += 1
    print(people)
    return answer + 1