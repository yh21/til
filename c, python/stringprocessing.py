message = 'Python is nice'
print(message.lower()) # 소문자
print(message.upper()) # 대문자
print(message[0].isupper()) # 대문자인지 확인

print(message.replace('Python', 'Java')) # python -> java
index = message.index('n')
print(index) # 처음으로 n이 나오는 index
index = message.index('n', index + 1)
print(index) # 두 번째로 n이 나오는 index

print(message.find('Java')) # 문자열이 없으면 -1 반환

print(message.count('n')) # message 안의 n 개수 반환