import sys
import math


def isPrime(n):

    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


def power(a, n, p):

    # Initialize result
    res = 1

    # Update 'a' if 'a' >= p
    a = a % p
    while n > 0:

        # If n is odd, multiply
        # 'a' with result
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p

            # n must be even now
            n = n // 2

    return res % p


# Utility function to store prime factors of a number
def primeFactorize(n):
    retval = list()
    while not (n & 1):
        retval.append(2)
        n = int(n / 2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            retval.append(i)
            n = int(n / i)
    if n > 2:
        retval.append(n)
    return set(retval)


# Function to find smallest primitive
# root of n
def findPrimitive(n):

    # Check if n is prime or not
    if isPrime(n) == False:
        return -1

    # Find value of Euler Totient function of n
    phi = n - 1

    # Find prime factors of phi and store in a set
    s = primeFactorize(phi)
    st = set()

    # Check for every number from 2 to phi
    for r in range(2, phi + 1):

        # Iterate through all prime factors of phi.
        # and check if we found a power with value 1
        flag = False
        for it in s:

            # Check if r^((phi)/primefactors)
            # mod n is 1 or not
            if power(r, phi // it, n) == 1:
                # st.add(r)
                flag = True
                break

        # If there was no power with value 1.
        if flag == False:
            st.add(r)

    return st
    # If no primitive root found
    return -1


def main():
    m = [int(i) for i in sys.argv[1:]][0]
    retval = sorted(findPrimitive(m))
    retval.insert(0, len(retval))
    print(" ".join([str(i) for i in retval]), end="")


if __name__ == "__main__":
    main()