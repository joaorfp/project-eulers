def square_sum(n):
    dict = {1: 0, 89: 0}
    sum = 0
    square = 0
    strn = str(n)
    # sumsqr = 0
    while sum != 89 or sum != 1:
        sum = 0
        
        for i in range(len(strn)):
            square = int(strn[i]) ** 2
            sum += square
        strn = str(sum)
        if sum == 89:
            if dict[sum] == 1:
                return True
            dict[sum] += 1
        elif sum == 1:
            if dict[sum] == 1:
                return False
            dict[sum] += 1
            
    

n = 0
count = 0
while n < 10000000:
    n += 1
    if square_sum(n):
        count += 1
print(count)