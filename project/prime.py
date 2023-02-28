def prime(num):
    if num > 1:
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
