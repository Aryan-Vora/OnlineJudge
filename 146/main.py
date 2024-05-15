import sys

input = sys.stdin.read
data = input().strip().split()

i = 0
while i < len(data):
    code = data[i]
    if code == "#":
        break

    s = list(code)
    n = len(s)

    k = -1
    for j in range(n - 1):
        if s[j] < s[j + 1]:
            k = j

    if k == -1:
        print("No Successor")
    else:
        l = -1
        for j in range(k + 1, n):
            if s[k] < s[j]:
                l = j

        s[k], s[l] = s[l], s[k]
        s = s[:k + 1] + s[k + 1:][::-1]
        print("".join(s))

    i += 1
