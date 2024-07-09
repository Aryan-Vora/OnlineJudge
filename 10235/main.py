import sys

def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

lines = sys.stdin.read().strip().split('\n')

for line in lines:
    original = int(line)
    reverse = int(line[::-1])
    if is_prime(original) and is_prime(reverse) and original != reverse:
        print(f'{line} is emirp.')
    elif is_prime(original):
        print(f'{line} is prime.')
    else:
        print(f'{line} is not prime.')
