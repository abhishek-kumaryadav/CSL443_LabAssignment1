import sys
from sys import stdout
from functools import lru_cache

sys.setrecursionlimit(100000000)

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
    print("{} {}".format(x, y))


if __name__ == "__main__":
    main()