def digit_sum(n):
    sum = n
    while (n > 0):
        sum += n % 10
        n = n // 10
    return sum

num = int(input())

for i in range(1, num):
    if num == digit_sum(i):
        print(i)
        break
    else:
        print('NONE') # T(n) = nlogn