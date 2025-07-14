n = int(input())
last_num = int((n ** 0.5))

for i in range(2, last_num + 1):
    if (n % i) == 0:
        print('Not prime number')
        break
    else:
        print('prime number')

