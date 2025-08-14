import sys

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()


    i = 0

    while i < len(s):
        if s[i] == 'O':
            print('[###OREO###]')
            i += 1
            continue
        
        if s[i] == 'R':
            print(' [--------] ')
            i += 2
            continue
        
        print()
        i += 1
        continue
    
