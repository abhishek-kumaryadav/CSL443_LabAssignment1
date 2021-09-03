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
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def find_divisors(arr):
    if len(arr) == 0:
        return
    else:
        gccd = arr[0]
        for i in range(1, len(arr) - 1):
            gccd = gcd(gccd, arr[i])
        divisors = set()
        i = 1
        while i * i <= gccd:
            if gccd % i == 0:
                divisors.add(i)
                divisors.add(int(gccd / i))
            i += 1
        return divisors


def main():
    arr = [int(i) for i in sys.argv[2:]]
    divisors = find_divisors(arr)
    print(" ".join(str(x) for x in sorted(divisors)))


if __name__ == "__main__":
    main()
