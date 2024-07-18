import sys

lines = sys.stdin.read().strip().split('\n')
for line in lines:
    if line == '0':
        break
    if int(line) % 11 == 0:
        print(f"{line} is a multiple of 11.")
    else:
        print(f"{line} is not a multiple of 11.")