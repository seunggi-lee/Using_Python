from collections import deque

def solution(s):
    if "{" not in s or "[" not in s or "(" not in s:
        return 0
    dic = {"(":")","[":"]","{":"}"}
    st = deque()
    cnt = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if s[j] =="{" or s[j] =="[" or s[j] =="(":
                st.append(s[j])
            else:
                if j == 0 or not st:
                    break
                t = st.pop()
                if dic[t] == s[j]:
                    if j == len(s) - 1:
                        cnt += 1
                    else:
                        continue
        s = s[1:] + s[0]
    return cnt