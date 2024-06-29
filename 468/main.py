import sys
from collections import Counter
lines = sys.stdin.readlines()
cases = int(lines[0].strip())
line_index = 2 

def decode_text(original_text, encoded_text):
    original_freq = Counter(original_text)
    encoded_freq = Counter(encoded_text)
    original_sorted = sorted(original_freq, key=original_freq.get, reverse=True)
    encoded_sorted = sorted(encoded_freq, key=encoded_freq.get, reverse=True)
    mapping = {encoded: original for original, encoded in zip(original_sorted, encoded_sorted)}
    decoded_text = ''.join(mapping.get(char, char) for char in encoded_text)
    return decoded_text

for i in range(cases):
    original_text = lines[line_index].strip()
    encoded_text = lines[line_index + 1].strip()
    print(decode_text(original_text, encoded_text))
    if i < cases - 1:  
        print()
    line_index += 3  

