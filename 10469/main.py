import sys
print('\n'.join(str(int(a) ^ int(b)) for a, b in (line.split() for line in sys.stdin.read().strip().split('\n'))))