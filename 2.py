
def problem21():
    amicables = []

    def sum_divs(i):
        divs = []
        for j in range(1, i):
            if (i % j == 0):
                divs.append(j)
        s = 0
        for item in divs:
            s += item
        return (s)

    for i in range(1, 10000):
        if (i in amicables):
            continue
        elif (i == sum_divs(sum_divs(i)) and sum_divs(i) != i):
            amicables.append(i)
            amicables.append(sum_divs(i))
    print(amicables)

    sum = 0
    for item in amicables:
        sum += item

    print(sum)


def problem22():
    names_list = []
    names_listed = []
    try:
        with open("0022_names.txt", 'r') as file:
            for line in file:
                names = line.split(",")
                names_list.extend(names)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    for item in names_list:
        names_listed.append(item[1:-1])

    names_listed.sort()

    def alpha_value(x):
        alphabet_dict = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
        s = 0
        for i in x:
            s += alphabet_dict[i]
        return s
    sum = 0
    index = 1
    for item in names_listed:
        sum += alpha_value(item)*index
        index += 1
    print(sum)


def problem23():
    def sum_div(x):
        s = 0
        for i in range(1, x):
            if (x % i == 0):
                s += i
        return (s)

    abundant = []
    for i in range(1, 28123):
        if (i < sum_div(i)):
            abundant.append(i)
    sum = 0
    # string = ""
    for i in range(1, 28124):
        test = True
        for item in abundant:
            if ((i-item) <= 0):
                break
            elif ((i-item) in abundant):
                test = False
                break
        if (test == True):
            # string += str(i)+"+"
            sum += i
    print(sum)
    # print(string)


def problem24():
    from itertools import permutations
    digits = '0123456789'
    all_permutations = list(permutations(digits))
    all_permutations_strings = [''.join(permutation)
                                for permutation in all_permutations]
    all_permutations_strings.sort()
    print(all_permutations_strings[999999])


def problem25():
    f = 1
    fdp = 1
    fp = 1
    i = 2
    while (len(str(f)) < 1000):
        i += 1
        f = fp+fdp
        fdp = fp
        fp = f
    print(i)


def problem26():
    for i in range(600, 660):
        ch = str(1/i)
        ch = ch[2:]
    # suspended due to shortness of number of decimals after zero


problem26()


def problem28(x):
    k = 2
    n = 1
    s = 1
    while (k < x):
        for i in range(4):
            n += k
            s += n
        k += 2

    print(s)


def problem29():
    dis_terms = []
    for i in range(2, 101):
        for j in range(2, 101):
            if (i**j not in dis_terms):
                dis_terms.append(i**j)
    print(len(dis_terms))


def problem30():
    num = []
    for i in range(2, 1000000):  # added zeros until the result isnt changing anymore
        ch = str(i)
        s = 0
        for j in ch:
            s += int(j)**5
        if (s == i):
            num.append(i)
    print(num)
    sum = 0
    for item in num:
        sum += item
    print(sum)


def problem32():
    def contains_digit(x, y):
        for l in str(x):
            for m in str(y):
                if (l == m):
                    return True
        return False

    def repeated_digit(x):
        for l in str(x):
            if (str(x).count(l) > 1 or l == "0"):
                return True
        return False
    products = []
    for i in range(1, 9999):
        for j in range(i, 9999):
            if (contains_digit(i, j) is True or repeated_digit(i) is True or repeated_digit(j) is True):
                continue
            elif (contains_digit(i*j, j) is True or contains_digit(i*j, i) is True or repeated_digit(i*j) is True):
                continue
            if (len(str(i))+len(str(j))+len(str(i*j)) == 9):
                print(i, j, i*j)
                if (i*j not in products):
                    products.append(i*j)
    s = 0
    for item in products:
        s += item
    print(s)


def problem33():
    num = 1
    den = 1
    for i in range(11, 100):
        if ((str(i))[-1] == "0"):
            continue
        for j in range(i+1, 100):
            if ((str(j))[-1] == "0"):
                continue
            for k in range(1, 10):
                ist = str(i)
                jst = str(j)
                if (ist.find(str(k)) >= 0 and jst.find(str(k)) >= 0):
                    if (ist.find(str(k)) == 0):
                        ist = ist[1]
                    else:
                        ist = ist[0]
                    if (jst.find(str(k)) == 0):
                        jst = jst[1]
                    else:
                        jst = jst[0]

                    if (i/j == int(ist)/int(jst)):
                        print(i, "/", j, ";", ist, "/", jst)
                        num *= i
                        den *= j
    print(num, den)
    for m in range(2, num):
        while ((den % m == 0) and (num % m == 0)):
            den = den//m
            num = num//m
        if (m > num):
            break
    print(num, "/", den)


def problem34():
    def fact(x):
        m = 1
        for j in range(1, x+1):
            m = m*j
        return m
    sum = 0
    for i in range(3, 100000):
        string = str(i)
        s = 0
        for l in string:
            s += fact(int(l))
        if (s == i):
            sum += i
            print(i)
    print(sum)


def problem35():
    import math

    def isprime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for divisor in range(5, int(math.sqrt(n)) + 1, 6):
            if n % divisor == 0 or n % (divisor + 2) == 0:
                return False
        return True
    count = 0
    for i in range(1, 1000000):
        test = True
        string = str(i)
        for j in range(len(string)):
            if (isprime(int(string)) is False):
                test = False
                break
            string = string[1:]+string[0]

        if (test == True):
            count += 1
    print(count)


problem35()
