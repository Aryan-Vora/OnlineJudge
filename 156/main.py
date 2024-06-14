import sys
input = sys.stdin.read()

lines = input.splitlines()
words = []

for line in lines:
    if line.strip() == "#":
        break
    words.extend(line.split())

normalized_dict = {}
original_words = {}

for word in words:
    normalized = ''.join(sorted(word.lower()))
    if normalized not in normalized_dict:
        normalized_dict[normalized] = 0
        original_words[normalized] = []
    normalized_dict[normalized] += 1
    original_words[normalized].append(word)

ananagrams = []

for norm_word, count in normalized_dict.items():
    if count == 1:
        ananagrams.append(original_words[norm_word][0])

ananagrams.sort()

for word in ananagrams:
    print(word)
