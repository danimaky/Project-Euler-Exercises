import time
from pprint import pprint

prime = []
i = 1
start = time.time()
while True:
    i += 1
    isprime = True
    for n in prime:
        if i % n == 0:
            isprime = False
    if isprime:
        prime.append(i)
    if len(prime) == 10001:
        break
print(prime[10000])
print("--- %s minutos ---" % ((time.time() - start) / 60))
