# gcd는 두 수의 나머지를 반복하여 구해서 나머지가 0이 되게 하는 수 a % b = 0 -> b가 최대공약수
# Lcm은 두 수의 곱를 최대공약수로 나눈 값


def gcd(a, b):
    if a <= b:
        a, b = b, a

    gcdNum = 0
    LcmNum = a * b
    while gcdNum == 0:
        n = a % b
        if n == 0:
            return b, int(LcmNum / b)
        else:
            a, b = b, n

    return gcdNum, LcmNum


print(gcd(12, 2))
print(gcd(78696, 19332))