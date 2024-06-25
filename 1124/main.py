import sys
lines = sys.stdin.readlines()

for line in lines:
    parts = line.split('=')
    print(parts[0] + "=" +   parts[1][:-1])