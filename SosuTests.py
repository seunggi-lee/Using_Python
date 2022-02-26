import math

def solution(nums):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                isTrue = True
                value = nums[i] + nums[j] + nums[k]
                for index in range(2, int(math.sqrt(value)) + 1):
                    if value % index == 0:
                        isTrue = False
                        break
                if isTrue:
                    result.append(value)
    answer = len(result)
    return answer

