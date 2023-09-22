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


def problem11():
    n = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
    li = n.split(" ")
    matrix = []
    top_value = []
    for i in range(20):
        row = []
        for j in range(i*20, i*20+20):
            row.append(int(li[j]))
        matrix.append(row)

    max_hor = 0
    m = 1
    index = ""
    for item in matrix:
        for i in range(20-4):
            jo = ""
            m = 1
            for k in range(4):
                m *= item[i+k]
                jo += str(item[i+k])+"*"
            if (max_hor < m):
                max_hor = m
                index = jo

    top_value.append(max_hor)
    print(f"horz {index[:-1]}={max_hor}")
    max_ver = 0
    indexv = ""
    for i in range(20):
        for item in range(20-4):
            w = 1
            yo = ""
            for k in range(4):
                w *= matrix[item+k][i]
                yo += str(matrix[item+k][i])+"*"
            if (w > max_ver):
                max_ver = w
                indexv = yo

    top_value.append(max_ver)
    print(f"vert {indexv[:-1]}={max_ver}")
    indexl = ""
    max_diag = 0
    for i in range(20-4):
        for j in range(20-4):
            l = 1
            lo = ""
            for k in range(4):
                l *= matrix[i+k][j+k]
                lo += str(matrix[i+k][j+k])+"*"
            if (max_diag < l):
                max_diag = l
                indexl = lo
    top_value.append(max_diag)
    print(f"diag left {indexl[:-1]}={max_diag}")
    indexr = ""
    max_diagr = 0
    for j in range(3, 20):
        for i in range(20-4):
            r = 1
            ro = ""
            for k in range(4):
                r *= matrix[i+k][j-k]
                ro += str(matrix[i+k][j-k])+"*"
            if (max_diagr < r):
                max_diagr = r
                indexr = ro
    top_value.append(max_diagr)
    print(f"diag right {indexr[:-1]}={max_diagr}")
    for item in top_value:
        max = top_value[0]
        if (item > max):
            max = item
    return (print(max))


problem11()
