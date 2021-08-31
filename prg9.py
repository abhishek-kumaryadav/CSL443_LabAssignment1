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
        print("INVALID ARGUMENTS")
        return
    a, m = [int(i) for i in sys.argv[1:]]
    print(multiplicativeOrder(a, m))


if __name__ == "__main__":
    main()