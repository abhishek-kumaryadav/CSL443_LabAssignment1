import sys
import math
from sys import stdout

int_r = lambda: int(sys.stdin.readline())
str_r = lambda: sys.stdin.readline().strip()
intList_r = lambda: list(map(int, sys.stdin.readline().strip().split()))
strList_r = lambda: list(sys.stdin.readline().strip())
jn = lambda x, l: x.join(map(str, l))
mul = lambda: map(int, sys.stdin.readline().strip().split())
mulf = lambda: map(float, sys.stdin.readline().strip().split())
ceil = lambda x: int(x) if (x == int(x)) else int(x) + 1
ceildiv = lambda x, d: x // d if (x % d == 0) else x // d + 1
flush = lambda: stdout.flush()
outStr = lambda x: stdout.write(str(x))
mod = 1000000007


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
    print(" ".join(str(i) for i in factors))


if __name__ == "__main__":
    main()