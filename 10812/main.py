import sys

def solve_superbowl_bets(test_cases):
    results = []
    for s, d in test_cases:
        if s < d or (s + d) % 2 != 0:
            results.append("impossible")
        else:
            score1 = (s + d) // 2
            score2 = s - score1
            results.append(f"{score1} {score2}")
    return results

lines = sys.stdin.read().strip().split('\n')
results = solve_superbowl_bets([tuple(map(int, line.split())) for line in lines[1:]])
for result in results:
    print(result)
