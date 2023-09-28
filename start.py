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


def problem12():
    k = 0
    div = 0
    x = 0
    while (div < 501):
        k += 1
        x += k
        div = 0
        for i in range(1, x+1):
            if (x % i == 0):
                div += 1
    print(x)


def problem13():
    li = """37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690"""

    listed = li.split("\n")
    s = 0
    for item in listed:
        s += int(item)
    s = str(s)
    print(s[:10])


def problem14(x):
    max = 0
    for i in range(1, x):
        k = 1
        ix = i
        while (ix != 1):
            if (ix % 2 == 0):
                ix = ix//2
                k += 1
            else:
                ix = (3*ix)+1
                k += 1
        if (max < k):
            max = k
            num = i
    print(f"the number with biggest chain under {x} is {num}")


def problem15(w):
    # w is the size of the grid (w=2 if the grid is 2*2)
    # the path takes (the grid size *2) steps I assumed
    # we gonna combine the number of steps with the nummber of possible moves (2 down and right) we use one and the other takes the place
    # we combine the number of steps with itshalf(because half the steps are down and half right)
    def fact(n):
        x = 1
        for i in range(1, n+1):
            x *= i
        return x
    steps_num = w*2

    n_pathes = (fact(steps_num)//(fact(steps_num-w)*fact(w)))
    print(n_pathes)


def problem16(x):
    # x is the exponential value of 2
    n = str(2**x)
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    print(s)


def problem17(w):
    numbers_dict = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "onethousand"
    }

    def num_to_alpha(x):
        ch = str(x)
        alpha = ""
        if (len(ch) == 1 or x == 1000 or (len(ch) == 2 and ch[0] == "1")):
            alpha = numbers_dict[x]
        elif (len(ch) == 2):
            alpha += numbers_dict[int(ch[0])*10]
            alpha += numbers_dict[int(ch[1])]
        elif (len(ch) == 3):
            alpha += numbers_dict[int(ch[0])]+numbers_dict[100]

            if (ch[1] == "1" or (ch[1] == "0" and ch[2] != "0")):
                alpha += "and"+numbers_dict[int(ch[1:])]
            elif (ch[1] != "0"):
                alpha += "and"+numbers_dict[int(ch[1])*10]
                alpha += numbers_dict[int(ch[2])]
        return alpha
    sentence = ""

    for i in range(1, w+1):
        sentence += num_to_alpha(i)
    print(sentence)
    return (print(len(sentence)))


def problem18():
    li = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    listed = li.split("\n")
    mylist = []
    for item in listed:
        l = item.split(" ")
        for it in l:
            it = int(it)
        mylist.append(l)

    k = len(mylist[-2])
    for i in range(-2, -16, -1):
        for j in range(k):
            if (int(mylist[i+1][j]) > int(mylist[i+1][j+1])):
                mylist[i][j] = int(mylist[i][j])+int(mylist[i+1][j])
            else:
                mylist[i][j] = int(mylist[i][j])+int(mylist[i+1][j+1])
        k = k-1

    print(mylist[0][0])


def problem19():
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    year = 1900
    day = 1

    def leap(x):
        leap = False
        if (x % 4 == 0):
            leap = True
        if (x % 100 == 0):
            leap = False
            if (x % 400 == 0):
                leap = True
        return leap

    for i in months:
        if (i == 2 and leap(year)):
            day += 29
        else:
            day += months[i]
    year += 1

    day = day % 7  # result is 2 its tuesday on 1 jan 1901

    sundays_first = 0
    while (year < 2001):
        for i in months:
            if (i == 2 and leap(year)):
                day += 29
            else:
                day += months[i]
            if (day % 7 == 0):
                sundays_first += 1
        year += 1

    print(sundays_first)


def problem20(x):
    def fact(w):
        n = 1
        for i in range(w, 0, -1):
            n *= i
        return str(n)

    ch = fact(x)
    s = 0
    for i in ch:
        s += int(i)

    print(s)


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


problem22()
