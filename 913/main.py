import sys

def sum_last_three_in_line(n):
    last = 2 * (n**2 + 2 * n) + 1
    second_last = 2 * (n**2 + 2 * n - 1) + 1
    third_last = 2 * (n**2 + 2 * n - 2) + 1
    return last + second_last + third_last

input = sys.stdin.read
data = input().split()

for line in data:
    if line.strip():
        line_num = (int(line) - 1) // 2
        result = sum_last_three_in_line(line_num)
        print(result)

