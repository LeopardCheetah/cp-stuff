#A-T/C-G


for i in range(int(input())):
    s = input().strip()
    t = ''

    for j in s:
        if j == 'A':
            t += 'T'
            continue
        
        if j == 'T':
            t += 'A'
            continue

        if j == 'C':
            t += 'G'
            continue

        t += 'C'
    
    print(t)