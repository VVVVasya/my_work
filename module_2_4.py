numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for is_prime in range(numbers[0], len(numbers) + 1):
    if is_prime > 1:
        for i in range(2, is_prime):
            if (is_prime % i) == 0:
                not_primes.append(is_prime)
                break
        else:
            primes.append(is_prime)
print(f'Primes:{primes}')
print(f'Not Primes:{primes}')
