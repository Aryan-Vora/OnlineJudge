def count_prime_factors(n):
	i = 2
	factors = set()
	while i * i <= n:
		while n % i == 0:
			factors.add(i)
			n //= i
		i += 1
	if n > 1:
		factors.add(n)
	return len(factors)

while True:
    n = int(input())
    if n == 0:
        break
    print(f"{n} : {count_prime_factors(n)}")
