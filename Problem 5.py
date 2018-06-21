# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import sys


def checkrules(number):
    return all(list(map(lambda i: number % i == 0, range(1, 21))))


def checknumbers(numbers):
    return all(list(map(lambda i: i == 1, numbers)))


lcm = 1
numbers = [i for i in range(2, 21)]
k = 2
while True:
    used = False
    for n in range(len(numbers)):
        if numbers[n] % k == 0:
            numbers[n] = numbers[n] // k
            used = True
    if used:
        lcm *= k
    else:
        k += 1
    if checknumbers(numbers):
        break
print(lcm)