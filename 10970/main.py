import sys

def min_cuts(m, n):
    return (m - 1) + m * (N - 1)

for line in sys.stdin:
    M, N = map(int, line.split())
    print(min_cuts(M, N))