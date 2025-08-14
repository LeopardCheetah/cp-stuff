# work in progress
# some tle

import sys

for _ in range (int(sys.stdin.readline())):
    l = int(sys.stdin.readline())
    ls = [int(a) for a in sys.stdin.readline().split()]
    lst = [int(c) for c in ls]

    # runtime = O(n^2)
    # mode = max(set(ls), key=ls.count)


    # idea: stochastic grad descend it
    l = 0
    r = 1

    while r < len(ls) and len(ls) > 1:
        if ls[l] != ls[r]:
            ls.pop(r)
            ls.pop(l)
            l = 0
            r = 1
            continue 
        
        r += 1
    
    if len(ls) < 2:
        # success lmao
        print(len(ls))
        continue 
    
    # count the max and see if there are more or less than half of the max
    mc = lst.count(ls[0])
    if mc*2 <= len(lst):
        # we are safe
        print(len(ls) % 2)
        continue  
    
    # we are not safe; there are more than half of one element in the list
    print(len(lst) - 2*(len(lst) - mc))
    

