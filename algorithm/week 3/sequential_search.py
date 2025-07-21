list = [30, 94, 15, 23, 19, 22, 98, 44, 52, 56]

target = 23

for i in range(0, len(list)):
    if (list[i] == target):
        print(i)
        break
else:
    print('Not Found')