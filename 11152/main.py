import sys
import math
lines = sys.stdin.read().strip().split('\n')
def calculate_areas(a, b, c):
    pass

for line in lines:
    a,b,c = map(int,line.split())
    A_sunflowers, A_violets, A_roses = calculate_areas(a,b,c)
    print(f"{A_sunflowers:.4f} {A_violets:.4f} {A_roses:.4f}")
