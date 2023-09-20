def problem1():
    s = 0
    for i in range(1000):
        if (i % 3 == 0 or i % 5 == 0):
            s += i
    return (print(f"s={s}"))


def problem2():

    li = [1, 2]
    s = 0
    i = 1
    while (li[-1] <= 4000000):
        li.append(li[i]+li[i-1])
        i += 1
    for item in li:
        if (item % 2 == 0):
            s += item
    return (print(f"s={s}"))


def problem3(x):
    import math
    prime_f = []

    def isprime(n):

        if (n <= 1):
            return False
        if (n <= 3):
            return True
        if (n % 2 == 0 or n % 3 == 0):
            for divisor in range(5, int(math.sqrt(n)) + 1, 6):
                if n % divisor == 0 or n % (divisor + 2) == 0:
                    return False
        return True

    k = 1
    while (x > 1):
        while (isprime(k) is False):
            k += 1
        while (x % k == 0):
            x = x//k
            prime_f.append(k)
        k += 1
    print(prime_f)
    return (print(prime_f[-1]))


problem3(600851475143)
