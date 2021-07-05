# Introduction to Lambda functions
# lambda args: expr

# palindrome = lambda str: str == str[::-1]
# print(palindrome('ana'))

# High order functions:
# filter(lambda_exp, iterable)
# map(lambda_exp, iterable)
# reduce(lambda_exp, iterable)

from functools import reduce

n = 20
x = 2


def filtering():
    mylist = [i for i in range(1, n+1)]
    odd = list(filter(lambda k: k % 2 != 0, mylist))
    print(type(odd), odd)


def mapping():
    mylist = [i for i in range(1, n+1)]
    squares = list(map(lambda k: k**x, mylist))
    print(type(squares), squares)


def reducing():
    mylist = [2]*5
    mult = reduce(lambda a, b: a*b, mylist)
    print(type(mult), mult)


if __name__ == '__main__':
    filtering()
    mapping()
    reducing()
