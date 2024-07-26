def count_squares(N):
    total_squares = 0
    for i in range(1, N + 1):
        total_squares += i * i
    return total_squares

import sys
input_data = sys.stdin.read().strip().split()

results = []
for n in input_data:
    N = int(n)
    if N == 0:
        break
    results.append(count_squares(N))

for result in results:
    print(result)

