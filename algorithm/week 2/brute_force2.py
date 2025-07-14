numbers = input()
numbers = numbers.split()

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

max = 500 ** 3

for i in range(1, max):
    count = 0
    for each in numbers:
        if (i % each) == 0:
            count += 1
    if (count >= 3):
        print(i)
        break

