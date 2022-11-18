from collections import deque
import math


def solution(fees, records):
    answer = []
    sRecords = sorted(records, key=lambda x: x[6:10])
    temp = deque()

    vehicleMoveInfor = {}
    for i in range(len(sRecords)):
        temp.append(sRecords[i].split(" "))
        if temp[i][1] not in vehicleMoveInfor:
            vehicleMoveInfor[temp[i][1]] = 1
            answer.append(0)
        else:
            vehicleMoveInfor[temp[i][1]] += 1
    # print("temp", temp)
    vehicleMoveInfor = list(vehicleMoveInfor.items())

    for i, v in enumerate(vehicleMoveInfor):
        fee = 0
        tempCnt = 0
        for j in range(v[1]):
            tempCnt += 1
            if tempCnt == 2:
                t2 = list(map(int, temp.popleft()[0].split(":")))
                t1 = list(map(int, temp.popleft()[0].split(":")))
                fee = (t1[0] - t2[0]) * 60 + t1[1] - t2[1]
                answer[i] += fee
                tempCnt = 0
            elif tempCnt != 2 and j == v[1] - 1:
                t = list(map(int, temp.popleft()[0].split(":")))
                fee = (23 - t[0]) * 60 + 59 - t[1]
                answer[i] += fee
                break
    # print("Cal Time : ", answer)
    result = [0] * len(answer)
    for i in range(len(answer)):
        result[i] = int(fees[1] + math.ceil((answer[i] - fees[0]) / fees[2]) * fees[3]) if answer[i] > fees[0] else \
        fees[1]
    # print(result)

    return result