import sys


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gccd, x, y = egcd(b % a, a)
        return gccd, y - (b // a) * x, x


def main():
    a, n = [int(i) for i in sys.argv[1:]]
    gccd, x, y = egcd(a, n)
    # print("a*{} + n*{} = {} = gcd({},{})".format(x, y, gccd, a, n))
    if gccd > 1:
        print("N", end="")
        # print("Multiplicative inverse of {}(mod {}) doesn't exist".format(a, n))
    else:
        print("Y {}".format((x % n + n) % n), end="")


if __name__ == "__main__":
    main()