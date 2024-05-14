import sys

input_data = sys.stdin.read()
cache = {}

def cycle(n):
    original_n = n
    steps = 0
    while n != 1:
        if n in cache:
            result = steps + cache[n]
            cache[original_n] = result
            return result
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    cache[original_n] = steps
    return steps

pairs = []
for line in input_data.strip().split('\n'):
    i, j = map(int, line.split())
    pairs.append([i, j])

for pair in pairs:
    start = min(pair[0], pair[1])
    finish = max(pair[0], pair[1])
    max_steps = 0
    for i in range(start, finish + 1):
        steps = cycle(i)
        max_steps = max(max_steps, steps)
    print(pair[0], pair[1], max_steps + 1) 
