def divisors(n):
    mylist = [i for i in range(1, n+1) if n%i==0]
    print(mylist)

def run():
    try:
        n = int(input("Digit a number: "))
        divisors(n)
        print("Exiting...")
    except ValueError:
        print("Only integers allowed!")

if __name__ == '__main__':
    run()