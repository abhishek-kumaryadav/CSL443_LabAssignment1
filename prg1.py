import sys


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
    print(" ".join(str(x) for x in sorted(divisors)), end="")


if __name__ == "__main__":
    main()
