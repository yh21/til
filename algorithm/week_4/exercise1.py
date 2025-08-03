time = list(map(int, input().split()))
time.sort()
total = 0

for i in range(0, len(time) - 1):
    total += time[i] * (len(time) - i - 1)

print(round(total / len(time)))