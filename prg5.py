import sys
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


def power(a, n, p):

    # Initialize result
    res = 1

    # Update 'a' if 'a' >= p
    # print("a = {} % {}".format(a, p))
    a = a % p
    while n > 0:

        # If n is odd, multiply
        # 'a' with result
        if n % 2:
            # print("res = ({} * {}) % {}".format(res, a, p))
            res = (res * a) % p
            # print("n = {} - 1".format(n))
            n = n - 1
        else:
            # print("a = ({} ** 2) % {}".format(a, p))
            a = (a ** 2) % p

            # n must be even now
            # print("n = {} // 2".format(n))
            n = n // 2

    return res % p


def main():
    a, x, n = [int(i) for i in sys.argv[1:]]
    output = power(a, x, n)
    print("{}".format(output))


if __name__ == "__main__":
    main()