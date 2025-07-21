i = 1
numbers = [8, 3, 4, 2, 6, 1, 9, 5, 7]
length = len(numbers)

while (i < length):
    j = i - 1
    key_value = numbers[i]
    while (j >= 0):
        if (key_value < numbers[j]):
            numbers[j + 1] = numbers[j]
        else:
            break
        j = j - 1
    numbers[j + 1] = key_value
    i = i + 1
    print(numbers)

print('END', numbers)