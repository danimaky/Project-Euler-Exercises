# a = 1
# b = 2
# a**2 + b**2 = c**2
# c = c ** (1/2)
# a + b + c = 1000
founded = False
for a in range(1, 999):
    for b in range(2, 999):
        c = a**2 + b**2
        c = c ** (1/2)
        if a + b + c == 1000:
            founded = True
            break
    if founded:
        break
print(a)
print(b)
print(c)
print(a*b*c)