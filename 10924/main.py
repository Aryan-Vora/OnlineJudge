import sys
import math

def is_prime(n):
    if n <= 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

for line in sys.stdin:
    s = line.strip()
    sum = 0
    for char in s:
        if 'a' <= char <= 'z':
            sum += ord(char) - ord('a') + 1
        elif 'A' <= char <= 'Z':
            sum += ord(char) - ord('A') + 27

    if is_prime(sum):
        print("It is a prime word.")
    else:
        print("It is not a prime word.")
