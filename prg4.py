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


def shareCommonDivisor(a, b):
    if a > b:
        temp = a
        a = b
        b = temp
    factors = set(primeFactorize(a))
    for f in factors:
        if b % f == 0:
            return True
    return False


def main():
    n = int(sys.argv[1])
    if n == 1:
        print("[], φ(1)=0")
    else:
        rrsm = set([1])
        for i in range(2, n):
            if not (shareCommonDivisor(i, n)):
                rrsm.add(i)
        retval = sorted(rrsm)
        retval.append(len(rrsm))
        print(" ".join(str(i) for i in retval), end="")
        # print("φ({})={}".format(n, len(rrsm)))


if __name__ == "__main__":
    main()