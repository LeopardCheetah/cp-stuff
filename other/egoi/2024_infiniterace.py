# 2024 EGOI
# Day 1 
# A. Infinite Race

import sys

n = int(sys.stdin.readline())
q = int(sys.stdin.readline())

# naive, we'll see how much memory this uses 
# memory isn't even an issue that much

def bsearch(ls, target):
    l = 0
    r = len(ls) - 1
    while l < r:
        m = (l + r) // 2
        if ls[m] == target:
            return m
        
        if ls[m] < target:
            l = m + 1
            continue 
        
        r = m - 1
        continue 
    
    return l

c = 0
bfr = []

for _ in range(q):
    k = int(sys.stdin.readline())
    
    if k > 0:
        if len(bfr) == 0:
            bfr.append(k)
            continue 

        if bfr[bsearch(bfr, k)] == k:
            # nice, we did another lap or whatever
            # clear buffer
            bfr = [k]
            c += 1
            continue

        # append to keep sorted list property
        ind = bsearch(bfr, k)
        if bfr[ind] > k:
            bfr.insert(ind, k)
            continue 

        bfr.insert(ind + 1, k)
    
    if k < 0:
        if len(bfr) == 0:
            continue 

        if bfr[bsearch(bfr, -k)] == -k:
            bfr.pop(bsearch(bfr, -k))
            continue


print(c)
