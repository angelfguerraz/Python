def intro():
    print("""Select n and x for (0...n)^x:\n""")
    n = int(input("n = "))
    x = int(input("x = "))
    return (n, x)  # return tuple


def run():
    t = intro()
    n = t[0]
    x = t[1]

    mydict = {
        # key: value
        i: i**x for i in range(1, n+1)
    }
    print(mydict)


if __name__ == '__main__':
    run()
