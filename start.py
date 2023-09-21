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


def problem4():
    def ispalindrome(x):
        x = str(x)
        pal = True
        for i in range(0, len(x)//2, 1):
            if (x[i] != x[-1-i]):
                pal = False
        return (pal)

    pal = []
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if (ispalindrome(i*j)):
                pal.append(i*j)
    max = pal[0]
    for item in pal:
        if item > max:
            max = item

    return print(max)


def problem5(x):
    k = 0
    while True:
        u = x-1
        k += 1
        while (u > 1):
            if (x*k % (u) == 0):
                u -= 1
            else:
                break
        if (u < 2):
            break
    print(x*k)


problem5(20)
