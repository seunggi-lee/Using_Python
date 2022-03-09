# 'A' = 65 'Z' = 90, 'a'= 97 'z'= 122, ' ' = 32
def solution(s, n):
    answer = ""
    for i in s:
        temp = chr(ord(i) + n)
        if i == " ":
            temp = " "
        elif ord('z') < ord(i) + n or ord('Z') < ord(i) + n and 65 <= ord(i) <= 90:
            temp = chr(ord(i) - 26 + n)
        answer += temp

    return answer