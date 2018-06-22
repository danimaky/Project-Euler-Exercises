import time
from pprint import pprint
def checkrules(number, numbers):
    return any(list(map(lambda i: number % i == 0, numbers)))
prime = []
i = 1
start = time.time()
while True:
    i += 1
    isprime = True
    for n in range(2, 11):
        if (i % n == 0 and i != n) or checkrules(i, prime):
            isprime = False
    if isprime:
        prime.append(i)
    if len(prime) == 10001:
        break
print(prime[10000])
print("--- %s minutos ---" % ((time.time() - start)/60))