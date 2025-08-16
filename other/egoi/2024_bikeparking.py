# 2024 EGOI
# Day 2
# B. Bike Parking

# 1s, 1gb
# score: 68/100
# test cases passed: 205/228 (tle on #206) -- im also not too sure how to make this more faster so :/



# note: if i want 100/100, i probably have to eliminate my reliance on arrays and figure out some other neat way to represent numbers and stuff



###########

import sys
from bisect import bisect_left as bs 

l = int(sys.stdin.readline())
spaces = [int(a) for a in sys.stdin.readline().strip().split()]
users = [int(a) for a in sys.stdin.readline().strip().split()]

# idea/alg:
# 1. try to map everyone to a higher pos
# 2. then look for equality
# 3. then shove everyone lower (aka they're a -1)

score = -1 * sum(users)

num_higher = 0
sptrs = [0]
svls = [0] # prefix sum arr
for ind in range(l):
    m = min(num_higher, users[ind])
    if m:
        num_higher -= m 
        users[ind] -= m
        score += m*2

        if num_higher == 0:
            sptrs = [0]
            svls = [0]
            if spaces[ind]:
                num_higher += spaces[ind]
                sptrs.append(ind)
                svls.append(spaces[ind] + svls[-1])
            
            continue 
        

        k = bs(svls, num_higher) + 1
        
        sptrs = sptrs[:k]
        svls = svls[:k]
        svls[-1] = num_higher
        # yay


    if spaces[ind]:
        num_higher += spaces[ind]
        sptrs.append(ind)
        svls.append(spaces[ind] + svls[-1])

    continue


# 2. look for equality
for i, v in enumerate(sptrs):
    if not i:
        continue

    score += min(users[v], svls[i] - svls[i - 1])

print(score)

