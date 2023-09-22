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


def problem6(x):
    s1 = 0
    s2 = 0
    for i in range(x+1):
        s1 += i
    s1 = s1**2
    for i in range(x+1):
        s2 += i**2
    s = s1-s2
    return (print(s))


def problem7(x):
    primes = 0
    k = 1
    while (primes < x):
        k += 1
        prime = True
        for i in range(2, int(k**0.5) + 1):
            if (k % i == 0):
                prime = False
        if (prime is True):
            primes += 1
    return (print(k))


def problem8(x):
    n = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    n = str(n)
    max = 1
    index = 0
    for i in range(0, 1000-x):
        m = 1
        for j in range(x):
            m *= int(n[j+i])
        if m > max:
            max = m
            index = i
    print(index)
    for i in range(index, index+x):
        print(str(n[i])+"*")
    return (print(max))


def problem9():
    m = 1
    # (biggest possible i =332)third of 1000 while i smaller than j and k 332+333+334
    for i in range(1, 332):
        for j in range(i+1, 500):  # half of 1000 while j smaller than 0+500+500
            for k in range(j+1, 1001):  # 0+0+1000
                if (i+j+k == 1000 and i**2+j**2 == k**2):
                    print(f"a={i} b={j} c={k}")
                    m = i*j*k
    return (print(m))


def problem10(x):
    m = 0
    li = []
    for i in range(x+1):
        prime = True
        if (i <= 1):
            prime = False

        for j in range(2, int(i**0.5)+1):
            if (i % j == 0):
                prime = False
                break

        if (prime == True):
            li.append(i)
            m += i
    return (print(m))
