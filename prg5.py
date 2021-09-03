import sys


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
    print("{}".format(output), end="")


if __name__ == "__main__":
    main()