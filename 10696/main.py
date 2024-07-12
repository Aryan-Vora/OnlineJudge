import sys

def f91(N):
    if N > 100:
        return N - 10
    else:
        return 91

lines = sys.stdin.read().strip().split('\n')
for line in lines:
    N = int(line)
    if N == 0:
        break
    print(f'f91({N}) = {f91(N)}')