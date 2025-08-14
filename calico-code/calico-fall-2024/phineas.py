import sys

def count(ls, obj):
    x = 0
    for i in ls[0]:
        if i == obj:
            x += 1
    
    return x

for _ in range(int(sys.stdin.readline())):
    m, n = map(int, sys.stdin.readline().strip().split())

    # m = number of rows
    # n = length of each row

    # 2x3:
    # . . .
    # . . .

    big_list = []
    for i in range(m):
        big_list.append([a for a in sys.stdin.readline().strip().split()])
    

    # just sum hashes

    hash_list = []

    for ls in big_list:
        hash_list.append(count(ls, '#'))
        new_list = [a - max(hash_list) for a in hash_list]
    
    for thing in range(len(new_list)):
        if hash_list[thing] == 0:
            new_list[thing] = 0

    if sum(new_list) == 0:
        print('ferb') # rectangle
        continue
    else:
        print('phineas')


    

