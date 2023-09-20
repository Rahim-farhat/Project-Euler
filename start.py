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


problem2()
