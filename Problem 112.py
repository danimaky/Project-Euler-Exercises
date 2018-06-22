# Parse the number right-to-left to find if it's bouncy.
def is_bouncy(num):
    has_incr_seq, has_decr_seq = False, False
    right_digit = num % 10
    num = num // 10

    while num > 0:
        left_digit = num % 10
        if left_digit < right_digit:
            has_incr_seq = True
        elif left_digit > right_digit:
            has_decr_seq = True
        right_digit = left_digit
        num = num // 10
        if has_incr_seq and has_decr_seq:
            return True
    return False

# Iterate through numbers until the bouncy count is 99%
# of the total count.
count = 0
i = 1
while count < 0.5 * i:
    i += 1
    if is_bouncy(i):
        count += 1
print(count)