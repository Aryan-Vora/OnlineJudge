import sys
import math

def calculate_flower_areas(a, b, c):
    #first calculate area of large circle
    hypotnuse = max(a, b, c)
    large_area = math.pi * ((hypotnuse/2) ** 2)
    #calculate area of triangle using herons formula
    s=(a+b+c)/2
    triangle_area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    large_area -= triangle_area
    #calculate area of small circle inscribed in the triangle and subtract triangle area
    small_area = math.pi * ((a+b+c) * (a+b-c) * (a-b+c) * (-a+b+c)) ** 0.5 / (2 * (a+b+c))
    triangle_area -= small_area
    print("{:.4f} {:.4f} {:.4f}".format(large_area, triangle_area, small_area))

import sys
input = sys.stdin.read().strip().split('\n')

for line in input:
    a, b, c = map(int, line.split())
    calculate_flower_areas(a, b, c)
