def exp(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return exp(x, n // 2) ** 2
    else:
        return (exp(x, n // 2) ** 2) * x
    
print(exp(5, 4))