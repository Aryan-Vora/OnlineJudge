import sys
for line in sys.stdin:
    n, k = map(int, line.split())
    smoked = 0
    butts = 0
    while n > 0:
        smoked += n  
        butts += n   
        n = butts // k 
        butts %= k   
    print(smoked)
