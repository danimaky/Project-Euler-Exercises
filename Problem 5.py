# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# def evaluar(number):
#     return all(list(map(lambda i: number % i == 0, range(1, 21))))


producto = 1
for i in range(2, 11):
    j = 2
    forward = True
    while forward:
        number = i
        if number % j == 0:
            number = number//j
            producto = producto * j
            if number == 1:
                forward = False
        else:
            j += 1
print(producto)