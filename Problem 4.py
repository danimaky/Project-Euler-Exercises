# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
max_number = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        value = i*j
        value_reversed = int(str(value)[::-1])
        if value == value_reversed and value>max_number:
            max_number = value_reversed
print(max_number)