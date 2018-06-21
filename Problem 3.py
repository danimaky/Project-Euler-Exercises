# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
number = 13195
number = 600851475143
i = 2
prime  = 0
while number != 1:
    if number % i == 0:
        prime = i
        number = number/prime
    i += 1
print(prime)