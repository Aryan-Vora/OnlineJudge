import sys
input = sys.stdin.read
data = input().strip().split()

for num in data:
    n = int(num)
    if n == 0:
        break
    sqrt_n = int(n ** 0.5)
    if sqrt_n * sqrt_n == n:
        print( "yes")
    else:
        print("no")
    

