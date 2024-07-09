import sys
lines = sys.stdin.read().strip().split('\n')
for line in lines:
    a, b = map(int, line.split())
    print(2*a*b)