def solution(s):
    answer = ""
    word_list = s.split(" ")
    for i, words in enumerate(word_list):
        for idx, word in enumerate(words):
            if idx % 2 == 0:
                answer += word.upper()
            else:
                answer += word.lower()
        if i != len(word_list) - 1:
            answer += ' '
    return answer