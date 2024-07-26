import sys

def will_box_fit(L, W, H):
    # Suitcase dimensions
    suitcase_size = 20
    # Check if the box fits in the suitcase
    if L <= suitcase_size and W <= suitcase_size and H <= suitcase_size:
        return True
    return False
input_data = sys.stdin.read().strip().split()
T = int(input_data[0])
results = []

index = 1
for case_number in range(1, T + 1):
    L = int(input_data[index])
    W = int(input_data[index + 1])
    H = int(input_data[index + 2])
    index += 3
    
    if will_box_fit(L, W, H):
        results.append(f"Case {case_number}: good")
    else:
        results.append(f"Case {case_number}: bad")

for result in results:
    print(result)

