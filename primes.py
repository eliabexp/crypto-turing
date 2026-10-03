import math

def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    i = 3
    sqrt = math.sqrt(n)

    while i <= sqrt:
        if n % i == 0:
            return False
        i += 2

    return True

def first_primes(count: int) -> list[int]:
    primes = []
    
    if count > 0:
        primes.append(2)

    n = 3
    while len(primes) < count:
        if is_prime(n):
            primes.append(n)
        n += 2

    return primes

def main():
    pass

if __name__ == "__main__":
    main()
