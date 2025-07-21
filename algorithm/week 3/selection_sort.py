i = 0
numbers = [8, 3, 4, 2, 6, 1, 9, 5, 7]
length = len(numbers)

while (i < length - 1):
    target = numbers[i:length]
    target_index = numbers.index(min(target))
    numbers[i], numbers[target_index] = numbers[target_index], numbers[i]
    i += 1
    print(numbers)

print('END', numbers)