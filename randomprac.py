from random import *

print(random()) # 0 ~ 1 사이의 임의의 난수
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 정수 난수
print(int(random() * 10) + 1) # 1 이상 10 이하의 임의의 정수 난수

print(randrange(1, 46)) # 1 이상 45 이하의 임의의 정수 난수
print(randint(1, 45)) # 1 이상 45 이하의 임으의 정수 난수