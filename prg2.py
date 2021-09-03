import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gccd, x, y = egcd(b % a, a)
        return gccd, y - (b // a) * x, x


def main():
    arr = [int(i) for i in sys.argv[1:]]
    gccd, x, y = egcd(arr[0], arr[1])
    print("{} {}".format(x, y), end="")


if __name__ == "__main__":
    main()