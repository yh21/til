numbers = [800, 32, 4, 122, 766, 12, 98, 53, 772, 8]
M = 3

def digit_func(n, d):
    if n >= (10 ** (d - 1)):
        return int(str(n)[-d])
    else:
        return 0
    
for i in range(1, M + 1):
    bucket = list()
    for j in range(0, 10):
        bucket.append(list())
    for number in numbers:
        bucket[digit_func(number, i)].append(number)
    numbers = list()
    for j in range(0, 10):
        for number in bucket[j]:
            numbers.append(number)

print(numbers)