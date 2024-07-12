import sys

lines = sys.stdin.read().strip().split("\n")
for line in lines[1:]:
    grades = list(map(int, line.split()))
    n = grades[0]
    grades = grades[1:]
    avg = sum(grades) / n
    above_avg = len([g for g in grades if g > avg])
    print(f"{above_avg/n*100:.3f}%")