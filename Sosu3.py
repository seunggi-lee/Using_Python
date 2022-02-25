minNum, maxNum = map(int, input().split())
result = []
num = 0.0

for i in range(minNum, maxNum+1):
    isTrue = True

    if i < 2:
        continue
    else:
        for j in range(2, int((i ** 0.5)) + 1):
            if i % j == 0:
                isTrue = False
                break
    if isTrue:
        result.append(i)

for i in result:
    print(i)
