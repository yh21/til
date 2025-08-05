def find_level(N):
    level = 0
    length = 3
    while (N >= length):
        level += 1
        length  = length * 2 + level
    return (level, length, N)

def find_type(level, length, N):
    if level == 0:
        if N == 1:
            print('A')
        elif N == 2:
            print('B')
        else:
            print('C')

    piece_length = (length - level) // 2
    if (N <= piece_length):
        return find_type(level - 1, piece_length, N)
    elif (N <= (piece_length + level)):
        return 'ieum'
    else:
        new_N = N - piece_length - level
        return find_type (level - 1, piece_length, new_N)
    
level, length, N = find_level(13)
print(find_type(level, length, N))