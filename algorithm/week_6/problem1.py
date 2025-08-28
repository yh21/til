# f(n) = f(n - 1) + f(n - 2) + f(n - 3)

test_list = [1, 2, 4]
for _ in range(0, 10000):
    test_list.append(-1)

def func(n):
    for i in range(3, n):
        test_list[i] = test_list[i - 1] + test_list[i - 2] + test_list[i - 3]
    return test_list[n - 1]

print(func(2023))