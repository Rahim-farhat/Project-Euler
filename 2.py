
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


problem23()
