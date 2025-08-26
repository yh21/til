def fibonacci(n):
    if fibo_list[n] != -1:
        return fibo_list[n]
    else:
        fibo_list[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fibo_list[n]

fibo_list = [1, 1]
for i in range(0, 10000):
    fibo_list.append(-1)

print(fibonacci(6))