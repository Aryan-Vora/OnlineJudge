import sys
lines = sys.stdin.readlines()
for line in lines:
    n, k, m = map(int, line.split())
    if n == 0 and k == 0 and m == 0:
        break

    victims = [True] * n
    official1, official2, victimCount = n - 1, 0, 0
    result = []

    while victimCount < n:
        for _ in range(m):
            official2 = (official2 - 1) % n
            while not victims[official2]:
                official2 = (official2 - 1) % n

        for _ in range(k):
            official1 = (official1 + 1) % n
            while not victims[official1]:
                official1 = (official1 + 1) % n

        if official1 == official2:
            result.append(f"{official1 + 1:3}")
            victimCount += 1
        else:
            result.append(f"{official1 + 1:3}{official2 + 1:3}")
            victimCount += 2

        victims[official1] = victims[official2] = False

    print(",".join(result))