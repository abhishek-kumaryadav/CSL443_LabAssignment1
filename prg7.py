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


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gccd, x, y = egcd(b % a, a)
        return gccd, y - (b // a) * x, x


def linearCongruence(A, B, N):

    A = A % N
    B = B % N
    x = 0
    y = 0

    # Find value of gcd, x, y
    gccd, x, y = egcd(A, N)

    # No solution
    if B % gccd != 0:
        print("N")
        return

    # Else, initialize the value of x0
    x0 = (x * (B // gccd)) % N
    if x0 < 0:
        x0 += N

    # Number of solutions
    print(gccd)
    # All the solutions
    for i in range(gccd):
        print((x0 + i * (N // gccd)) % N, end=" ")


def main():
    a, b, m = [int(i) for i in sys.argv[1:]]
    linearCongruence(a, b, m)


if __name__ == "__main__":
    main()