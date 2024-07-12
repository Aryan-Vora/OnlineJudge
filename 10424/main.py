import sys

def calculate_love(name1, name2):
    def name_sum(name):
        return sum((ord(char.lower()) - 96) for char in name if char.isalpha())
    
    sum1 = name_sum(name1)
    sum2 = name_sum(name2)
    
    while sum1 > 9:
        sum1 = sum(map(int, str(sum1)))
    while sum2 > 9:
        sum2 = sum(map(int, str(sum2)))
    
    ratio = min(sum1, sum2) / max(sum1, sum2) * 100
    return f"{ratio:.2f} %"

lines = sys.stdin.read().strip().split('\n')

for i in range(0, len(lines), 2):
    print(calculate_love(lines[i], lines[i+1]))
    