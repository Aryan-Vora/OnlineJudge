import sys
input = sys.stdin.read().strip()
lines = input.split("\n")
results = []

for line in lines:
    if line.strip() == "":
        continue
    bottles = list(map(int, line.split()))

    bin1 = bottles[0:3]
    bin2 = bottles[3:6]
    bin3 = bottles[6:9]
    
    configurations = [
        ("BCG", bin1[0], bin2[2], bin3[1]),  
        ("BGC", bin1[0], bin2[1], bin3[2]),  
        ("CBG", bin1[2], bin2[0], bin3[1]),  
        ("CGB", bin1[2], bin2[1], bin3[0]),  
        ("GBC", bin1[1], bin2[0], bin3[2]),  
        ("GCB", bin1[1], bin2[2], bin3[0])
    ]
    
    min_moves = float('inf')
    best_config = ""
    
    for config in configurations:
        moves = (sum(bin1) + sum(bin2) + sum(bin3)) - sum(config[1:])  # Total bottles minus the ones we keep
        if moves < min_moves or (moves == min_moves and config[0] < best_config):
            min_moves = moves
            best_config = config[0]
    
    results.append(f"{best_config} {min_moves}")

for result in results:
    print(result)

