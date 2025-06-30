def prime_number(num):
    for i in range(2, num):
        if (num % i) == 0 :
            return False
    return True
    
print(prime_number(17))

def triple_max(a, b ,c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else :
        return c

print(triple_max(12, 17, 3))

def list_sum(input_list):
    total = 0
    for i in input_list:
        total += i
    return total

a = [1, 2, 3, 5, 6]
print(list_sum(a))
