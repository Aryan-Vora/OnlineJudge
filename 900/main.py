import sys

input_data = sys.stdin.read().strip().split()
lengths = list(map(int, input_data))

fib = [0] * 51
fib[0], fib[1] = 1, 1

for i in range(2, 51):
    fib[i] = fib[i-1] + fib[i-2]

for length in lengths:
    if length == 0:
        break
    print(fib[length])