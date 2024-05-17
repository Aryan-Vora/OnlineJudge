import sys
input = sys.stdin.read().strip()
lines = input.split("\n")
result = []
frequency = []
for i in range(1, int(lines[0])+1):
    for j in lines[i]:
        if j.isalpha():
            if j.upper() in frequency:
                result[frequency.index(j.upper())] = (result[frequency.index(
                    j.upper())][0], result[frequency.index(j.upper())][1]+1)
            else:
                frequency.append(j.upper())
                result.append((j.upper(), 1))
result.sort(key=lambda x: (-x[1], x[0]))
for i in result:
    print(i[0], i[1])
