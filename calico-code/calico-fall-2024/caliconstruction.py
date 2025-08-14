import sys

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    s = s.lower()


    
    # calico == ccalio

    # l
    # i + h
    # o
    # a
    # 2x (u/n/c)

    x = [0, 0, 0, 0, 1, 0] #a, o, l, i + h, c + n + u

    for i in s:
        if i == 'a':
            x[0] += 1
            continue
        
        if i == 'o':
            x[1] += 1
            continue
        
        if i == 'l':
            x[2] += 1
            continue
        
        if i == 'i' or i == 'h':
            x[3] += 1
            continue
        
        if i == 'c' or i == 'n' or i == 'u':
            x[4] += 1
            continue 
        
        x[5] += 1
        continue

    if x[5] > 0:
        print('-1')
        continue
    
    x[4] = x[4] // 2
    print(max(x))

