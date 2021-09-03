import sys
import math


def primeFactorize(n):
    retval = list()
    while not (n & 1):
        retval.append(2)
        n = int(n / 2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            retval.append(i)
            n = int(n / i)
    if n > 2:
        retval.append(n)
    return retval


def main():
    n = int(sys.argv[1])
    factors = primeFactorize(n)
    print(" ".join(str(i) for i in factors), end="")


if __name__ == "__main__":
    main()