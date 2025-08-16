# only took me a few speedups and 10 submissions

import sys

for _ in range(int(sys.stdin.readline())):
    l = int(sys.stdin.readline())
    ls = [int(a) for a in sys.stdin.readline().strip().split()]

    # time for some risky business
    arr = [a for a in range(l, 0, -1)] # also in reverse now
    arrt = [] # sorted in reverse

    la = [] # min permute
    lb = [] # max permute
    step = 0

    # cheese
    if ls == arr[::-1]:
        for c in arr[::-1]:
            sys.stdout.write(str(c) + ' ')
        sys.stdout.write('\n')
        for d in arr[::-1]: 
            sys.stdout.write(str(d) + ' ')
        sys.stdout.write('\n')
        continue

    for i in ls:
        if i > step:
            la.append(i)
            lb.append(i)
            
            # print(arr, i, step)
            # arr = [a for a in range(i - 1, step, -1)] + arr
            # arr += [a for a in range(i - 1, step, -1)]
            arr.pop(l - i)

            arrt += [a for a in range(step + 1, i)]
            # arrt.pop()

            step = i
            continue 
        
        # i = step -- things haven't changed
        # for lsa just add the first element
        la.append(arr.pop()) # yipeee
        # fast since .pop() is apparently O(1) so we look to be doing ok

        # lb: find maximal thing so just pop off b pointer
        lb.append(arrt.pop())
        continue 
    
    for c in la:
        sys.stdout.write(str(c) + ' ')
    sys.stdout.write('\n')
    for d in lb: 
        sys.stdout.write(str(d) + ' ')
    sys.stdout.write('\n')
