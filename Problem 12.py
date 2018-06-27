def countmultiples(number):
    count = len([i for i in range(1, number+1) if number % i == 0])
    print(count)
    return count

i = 1000
while True:
    triangulenum = 0
    for n in reversed(range(i+1)):
        triangulenum += n
    if countmultiples(triangulenum) > 500:
        break
    i += 1
print(triangulenum)