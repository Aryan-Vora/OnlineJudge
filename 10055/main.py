import sys
lines = sys.stdin.read().strip().split('\n')

for line in lines:
    a, b = map(int, line.split())
    print(abs(a - b) if a > b else abs(b - a))