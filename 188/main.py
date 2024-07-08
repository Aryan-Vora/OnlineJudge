import sys

CHAR_VALUES = [ord(char) - ord('a') + 1 for char in "abcdefghijklmnopqrstuvwxyz"]

def word_to_int(word):
    """Convert a word to its corresponding integer value using a precomputed array."""
    value = 0
    for char in word:
        value = value * 32 + CHAR_VALUES[ord(char) - ord('a')]
    return value

def find_min_C(words):
    """Find the minimum C such that the hash function is perfect."""
    n = len(words)
    int_words = [word_to_int(word) for word in words]
    C = 1  
    while True:
        seen = set()
        for w in int_words:
            hash_value = (C // w) % n
            if hash_value in seen:
                break
            seen.add(hash_value)
        else:
            return C
        C += 1

input_lines = sys.stdin.read().strip().split("\n")

for line in input_lines:
    words = line.split()
    C = find_min_C(words)
    print(line)
    print(C)
    print()
