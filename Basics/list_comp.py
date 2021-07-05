def intro():
    print("""Select n and x for (0...n)^x:\n""")
    n = int(input("n = "))
    x = int(input("x = "))
    return (n, x)  # return tuple


def run():
    # List comprehension:
    mylist = [i**2 for i in range(1, 100+1) if i % 3 != 0]

    # for i in range(1, n+1):
    #     if (i % 3 != 0):
    #         mylist.append(i**2)

    print(mylist)


def challenge():
    t = intro()
    n = t[0]  # 100
    x = t[1]  # 2
    mylist = [i for i in range(1, n+1) if i %
              4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(mylist)


if __name__ == '__main__':
    challenge()
