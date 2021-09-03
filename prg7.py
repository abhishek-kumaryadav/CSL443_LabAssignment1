import sys


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
        print("N", end="")
        return

    # Else, initialize the value of x0
    x0 = (x * (B // gccd)) % N
    if x0 < 0:
        x0 += N
    retval = [str((x0 + i * (N // gccd)) % N) for i in range(gccd)]
    retval.insert(0, str(len(retval)))
    retval.insert(0, "Y")
    print(" ".join(retval), end="")
    # Number of solutions
    # print(gccd)
    # All the solutions
    # for i in range(gccd):
    # print((x0 + i * (N // gccd)) % N, end=" ")


def main():
    a, b, m = [int(i) for i in sys.argv[1:]]
    linearCongruence(a, b, m)


if __name__ == "__main__":
    main()