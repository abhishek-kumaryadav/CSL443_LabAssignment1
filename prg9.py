import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def multiplicativeOrder(a, m):
    if gcd(a, m) != 1:
        return -1

    # result store power of a that rose to the power m-1
    result = 1

    i = 1
    while i < m:
        # modular arithmetic
        result = (result * a) % m
        # return
        if result == 1:
            return i
        # increment
        i += 1

    return -1


def main():
    if (len(sys.argv)) != 3:
        print("INVALID ARGUMENTS", end="")
        return
    a, m = [int(i) for i in sys.argv[1:]]
    print(multiplicativeOrder(a, m), end="")


if __name__ == "__main__":
    main()