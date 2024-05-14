import sys
input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
matrix = []
index = 1
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(data[index]))
        index += 1
    matrix.append(row)

result = float('-inf')
for left in range(N):
    temp_sum = [0] * N
    for right in range(left, N):
        for i in range(N):
            temp_sum[i] += matrix[i][right]
        current_max = temp_sum[0]
        max_ending_here = temp_sum[0]
        for j in range(1, N):
            max_ending_here = max(max_ending_here + temp_sum[j], temp_sum[j])
            current_max = max(current_max, max_ending_here)
        result = max(result, current_max)
print(result)
