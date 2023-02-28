def is_lychrel_number(n):
    iteration = 0
    n1 = int(str(n)[::-1])
    if n == n1:
        return False
    else:
        sum = n + n1
        reverse_sum = int(str(sum)[::-1])
        while sum != reverse_sum:
            iteration += 1
            sum += reverse_sum
            reverse_sum = int(str(sum)[::-1])
            if iteration >= 50:
                return True
            if sum == reverse_sum:
                return False
                
n = 0
count = 0

while n < 10000:
    n += 1
    if is_lychrel_number(n):
        count += 1
        
print(count)
