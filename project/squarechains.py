def square_sum(n):
    dict = {1: 0, 89: 0}
    sum = 0
    square = 0
    strn = str(n)
    while sum != 89 or sum != 1:
        sum = 0
        # loops thru the numbers given
        for i in range(len(strn)):
            # gets the square root of each number given
            square = int(strn[i]) ** 2
            # sum each number
            sum += square
        strn = str(sum)

        # checks if the sum reaches 89 or 1 (it will, eventually)
        if sum == 89:

            # checks if 89 or 1 had already been reached
            if dict[sum] == 1:
                return True
            # iterates one in that specified address in the dict(1 or 89)
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