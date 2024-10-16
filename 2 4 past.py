numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = 0
while is_prime == True:
    for is_prime in numbers:
        for i in is_prime:
            if is_prime % i == 0:
                print(f'primes:{primes}')
                primes.append(is_prime)
                break
    else:
        not_primes.append(i)
    print(f'Primes:{primes}')
print(not_primes)