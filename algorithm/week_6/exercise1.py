# f(n) = f(n - 1) + f(n - 2)

n = int(input())

test_list = [1, 2]
for _ in range(0, 10000):
    test_list.append(-1)

def func(n):
    if test_list[n] != -1:
        return test_list[n]
    else:
        test_list[n] = func(n - 1) + func(n - 2)
        return test_list[n]
    
print(func(n - 1))