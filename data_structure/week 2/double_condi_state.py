score_ma = int(input('Enter your math score: '))
score_py = int(input('Enter your python score: '))
average = (score_ma + score_py) / 2

if (average >= 60):
    if (score_py < 40) or (score_ma < 40):
        print('non pass')
    else:
        print('pass')
else:
    print('non pass')