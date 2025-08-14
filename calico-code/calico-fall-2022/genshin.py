# interactive problems are cool

import sys

for _ in range(int(sys.stdin.readline())):
    # do an interaction
    # + 60, - 160

    n = int(sys.stdin.readline())

    # 15 chars long
    i = ''
    while i != 'you got: baizhu':
        if n < 160:
            print('buy')
            sys.stdout.flush()
            i = sys.stdin.readline().strip()
            n += 60
            continue

        print('wish')
        sys.stdout.flush()
        n -= 160
        i = sys.stdin.readline().strip()
    
    # success
    i = sys.stdin.readline()