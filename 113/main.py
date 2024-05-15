import sys
input = sys.stdin.read().strip()
lines = input.split("\n")
pairs = []
for i in range(0, len(lines), 2):
    pairs.append((lines[i], lines[i + 1]))

for pair in pairs:
    n = int(pair[0])
    number = int(pair[1])
    print(int(round(number ** (1/n))))
