def eratos(num):
    isPrime = [True] * num

    for i in range(2, int(num ** 0.5) + 1):
        if isPrime[i] == True:
            for j in range(2 * i, num, i):
                isPrime[j] = False

    result = [i for i in range(2, len(isPrime)) if isPrime[i]]

    return result


n = 100

print(eratos(n))

m = 10000

print(eratos(m))
