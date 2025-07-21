numbers = [8, 3, 4, 2, 6, 1, 9, 5, 7]
i = 1
length = len(numbers)

while (i < length):
    swap_check = False
    j = 0
    while (j < length - i):
        if (numbers[j] > numbers[j + 1]):
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swap_check = True
        j = j + 1
    if (swap_check == False):
        break
    i += 1
    print(numbers)

print('END', numbers)