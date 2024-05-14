import sys

# Read input data from stdin
input_data = sys.stdin.read()

# Cache to store computed cycle lengths
cache = {}

# Function to compute cycle length of a number
def cycle(n):
    original_n = n
    steps = 0
    while n != 1:
        # Check if cycle length for n is already computed
        if n in cache:
            result = steps + cache[n]
            cache[original_n] = result
            return result
        # Apply 3n + 1 or n/2 rule
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    # Store the computed cycle length in cache
    cache[original_n] = steps
    return steps

# Parse input data and store pairs of integers
pairs = []
for line in input_data.strip().split('\n'):
    i, j = map(int, line.split())
    pairs.append([i, j])

# Compute maximum cycle length for each pair and print results
for pair in pairs:
    start = min(pair[0], pair[1])
    finish = max(pair[0], pair[1])
    max_steps = 0
    # Find maximum cycle length within the range
    for i in range(start, finish + 1):
        steps = cycle(i)
        max_steps = max(max_steps, steps)
    # Print the pair and maximum cycle length
    print(pair[0], pair[1], max_steps + 1)