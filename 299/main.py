import sys
lines = sys.stdin.readlines()
train_length = int(lines[0])
def printsolution(S):
    print("Optimal train swapping takes", S, "swaps.")
highest = 0
for i in range(1, len(lines)):
    if i % 2 == 1:
        highest = lines[i]
        continue
    else:
        swaps = 0
        trains = list(map(int, lines[i].split()))
        for j in range(len(trains)):
            for k in range(j+1, len(trains)):
                if trains[j] > trains[k]:
                    temp = trains[j]
                    trains[j] = trains[k]
                    trains[k] = temp
                    swaps += 1
        printsolution(swaps)
