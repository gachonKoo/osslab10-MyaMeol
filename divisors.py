import sys

def get_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(" ".join(map(str, get_divisors(n))))
