def solution(s):
    answer = s
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(num_list)):
        if num_list[i] in s:
            answer.replace(num_list[i], str(i))
            print(answer)
    return answer

solution("one4seveneight")