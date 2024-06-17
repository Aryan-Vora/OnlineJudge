import sys
lines = sys.stdin.read().strip().split('\n')
N = []
for line in lines:
    if line == "0":
        break
    N.append(int(line))

for n in N:
    # we are going to go through all m values until we find one that works
    for m in range(1, n):
        values = [i for i in range(1, n + 1)]
        x = 0
        # we are going to go through it until we reach 13
        while (len(values) > 1 and values[x] != 13):
            values.pop(x)
            x += m - 1
            if x >= len(values):
                x %= len(values)

        if (values == [13]):
            print(m)
            break
