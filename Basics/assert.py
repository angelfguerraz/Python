def divisors(n):
    mylist = [i for i in range(1, n+1) if n % i == 0]
    print(mylist)


def run():

    n = input("Digit a number: ")
    assert int(n) >= 0, "Integer must be non-negative"
    assert n.isnumeric(), "An integer is required"
    divisors(int(n))
    # print("Exiting...")


if __name__ == '__main__':
    run()
