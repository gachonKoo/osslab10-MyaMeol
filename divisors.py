import sys

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python divisors.py <number>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        result = get_divisors(n)
        print(" ".join(str(x) for x in result))
    except Exception as e:
        print("Error:", e)
