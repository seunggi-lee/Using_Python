def solution(clothes):
    answer = 1
    clothes_dic = {}
    for cloth in clothes:
        temp = cloth[1]
        if temp in clothes_dic:
            clothes_dic[temp] += 1
        else:
            clothes_dic[temp] = 1

    for i in clothes_dic.values():
        answer *= (i + 1)
    return answer - 1

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])