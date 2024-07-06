import sys
input = sys.stdin.read
data = input().strip().split('\n')

def is_jolly_jumper(sequence):
    n = sequence[0]
    if n == 1:
        return "Jolly"

    differences = set()
    for i in range(1, n):
        diff = abs(sequence[i] - sequence[i+1])
        if diff < 1 or diff >= n:
            return "Not jolly"
        differences.add(diff)

    for i in range(1, n):
        if i not in differences:
            return "Not jolly"
    
    return "Jolly"



results = []
for line in data:
    sequence = list(map(int, line.split()))
    results.append(is_jolly_jumper(sequence))

for result in results:
    print(result)

