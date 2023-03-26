def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_lychrel_number(n):
    for i in range(50):
        n += int(str(n)[::-1])
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
