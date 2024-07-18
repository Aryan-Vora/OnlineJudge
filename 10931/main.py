import sys
lines = sys.stdin.read().strip().split('\n')

for line in lines:
    if int(line) == 0:
        break
    binary = bin(int(line))[2:]
    print(f"The parity of {binary} is {binary.count('1')} (mod 2).")