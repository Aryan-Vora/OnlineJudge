import sys
lines = sys.stdin.read().split("\n")[:-1]
#find longest line
max_len = 0
for i in range(len(lines)):
    if len(lines[i]) > max_len:
        max_len = len(lines[i])

for i in range(max_len):
    temp = ""
    for j in range(len(lines)):
        if i < len(lines[j]):
            temp += lines[j][i]
    print(temp)