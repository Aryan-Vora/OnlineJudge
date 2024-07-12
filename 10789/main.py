import sys

def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True

def count_frequency(s):
	freq = {}
	for char in s:
		if char in freq:
			freq[char] += 1
		else:
			freq[char] = 1
	return freq

def prime_frequency_chars(s):
	freq = count_frequency(s)
	result = ''
	for char in sorted(freq.keys()):
		if is_prime(freq[char]):
			result += char
	return result if result else 'empty'

lines = sys.stdin.read().strip().split('\n')
T = int(lines[0])
for i in range(1, T + 1):
	result = prime_frequency_chars(lines[i])
	print(f'Case {i}: {result}')