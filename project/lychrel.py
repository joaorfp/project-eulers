def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_lychrel_number(n):
    # loop thru 50 indexes (there is no number under 10000 that takes more than 50 iterations)
    for i in range(50):
        # n sums itself with its reverse
        n += int(str(n)[::-1])
        # We want number that dont make a palindrome
        if is_palindrome(n):
            return False
    return True

count = 0
n = 0
while n < 10000:
    n += 1
    if is_lychrel_number(n):
        count += 1

print(count)
