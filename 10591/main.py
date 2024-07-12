def is_happy_number(n):
	seen = set()
	while n not in seen:
		seen.add(n)
		n = sum(int(digit)**2 for digit in str(n))
		if n == 1:
			return True
	return False

test_cases = int(input())
for i in range(1, test_cases + 1):
    n = int(input())
    if is_happy_number(n):
        print(f"Case #{i}: {n} is a Happy number.")
    else:
        print(f"Case #{i}: {n} is an Unhappy number.")
