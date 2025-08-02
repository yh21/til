coin = [500, 100, 50, 10]

money = int(input())
coin_count = 0

if (money % 10) == 0:
    for each_coin in coin:
        while money >= each_coin:
            coin_count += 1
            money -= each_coin
    print(coin_count)
else:
    print("Fail")