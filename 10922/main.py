import sys

def sum_digits(n):
    depth = 0
    original_n = n  # Store the original number
    while n >= 10 or original_n == 9:
        n = sum(int(digit) for digit in str(n))
        depth += 1
        original_n = 0  # Reset original_n after the first iteration
    return n, depth

lines = sys.stdin.read().strip().split('\n')
for line in lines:
    if line == '0':
        break
    n = int(line)
    digit_sum, depth = sum_digits(n)
    if digit_sum == 9:
        print(f'{n} is a multiple of 9 and has 9-degree {depth}.')
    else:
        print(f'{n} is not a multiple of 9.')