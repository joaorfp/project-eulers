def prime(num):
    if num > 1:
        # loops to check whether the param number can be divided by the index and have 0 as remaining.
        # The int(num ** 0.5) + 1 makes sure that the loop does not reach a very large number. The index dont need to go after the square root + 1 of the number,
        # if it reached this number and the condition was not satisfied, it wont ever be.
        for index in range(2, int(num ** 0.5) + 1):
            if (num % index) == 0:
                return False
        
        return True

count = 0
num = 1

while True:
    num += 1
    if prime(num):
        count += 1
        if count == 10001:
            print(num)
            break
