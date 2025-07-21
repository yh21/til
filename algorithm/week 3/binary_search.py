list = [15, 19, 22, 23, 30, 44, 52, 56, 94, 98]

target = 29
left = 0
right = len(list) - 1

while(True):
    mid = (left + right) // 2
    if (target == list[mid]):
        print(mid)
        break
    elif (target < list[mid]):
        right = mid - 1
    else:
        left = mid + 1
    if (left > right):
        print('Not Found')
        break
