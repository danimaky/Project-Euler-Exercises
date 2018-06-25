# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
primes = []
for i in range(2, 2000000):
    prime = True
    for number in primes:
        if i % number == 0:
                prime = False
                break
    if prime:
        primes.append(i)
        print(i)
print(sum(primes))