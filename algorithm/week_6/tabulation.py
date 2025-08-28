fibo_list = [1, 1]
for _ in range(0, 10000):
    fibo_list.append(-1)

def fibonacci(n):
    for i in range(2, n + 1):
        fibo_list[i] = fibo_list[i - 1] + fibo_list[i - 2]
    return fibo_list[n]

print(fibonacci(6))