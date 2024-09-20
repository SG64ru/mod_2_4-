numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 307]
primes = []
not_primes = []
for num in numbers:
    if num == 1:
        continue
    if num != 2 and num % 2 ==0:
        not_primes.append(num)
        continue
    else:
        for del_ in range(3, num//2 + 1, 2):
            if num % del_ == 0:
                not_primes.append(num)
                break
            else:
                primes.append(num)
                break
print(f"primes: {primes}")
print(f"not_primes: {not_primes}")




