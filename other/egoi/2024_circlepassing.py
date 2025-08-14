# 2024 EGOI
# Day 2
# A. Infinite Race

# ac'd 100/100 first try!
# im very happy about this submission :)

import sys


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



n, m, q = map(int, sys.stdin.readline().split())
friends = [int(a) for a in sys.stdin.readline().split()]

for c in range(m):
    friends.append(friends[c] + n)


for _ in range(q):
    # test cases!

    x, y = map(int, sys.stdin.readline().split())
    
    # 3 options
    # 1. naive -- just go along arc
    # 2. take the best friends to the left + go from there
    # 3. take the best friend from right + go from there


    naive = 0
    if y - x < 0:
        naive = min(x - y, y - x + 2*n)
    else:
        naive = min(y - x, x - y + 2*n)


    #############3

    # for now pathing will be x -> y
    left_arc = 1
    # move "left" (4 -> 3 -> 2 -> 1 -> 0 -> 2n - 1 -> ...) until first friend is reached
    right_arc = 1 # 1 added since the jump counts as a pass
    fcf = bsearch(friends, x)

    lj_end = -1
    rj_end = -1

    if friends[fcf] == x:
        # nice! add 0.
        lj_end = (x + n) % (2*n)
        rj_end = lj_end
        pass 
    else:
        # we're at the tail end so wrap around i guess
        if x - friends[fcf] > 0:
            # go to the left
            left_arc += x - friends[fcf]
            lj_end = (friends[fcf] + n) % (2*n)
        elif x - friends[fcf - 1] < 0:
            left_arc += x + 2*n - friends[fcf - 1]
            lj_end = (friends[fcf - 1] + n) % (2*n)
        else:
            left_arc += x - friends[fcf - 1]
            lj_end = (friends[fcf - 1] + n) % (2*n)

        # right arc processing
        if x > friends[-1]:
            # gotta go chase friends[0]
            right_arc += (2*n - x) + friends[0]
            rj_end = (friends[0] + n) % (2*n)
        elif x < friends[fcf]:
            right_arc += friends[fcf] - x
            rj_end = (friends[fcf] + n) % (2*n)
        else:
            right_arc += friends[fcf + 1] - x
            rj_end = (friends[fcf + 1] + n) % (2*n)
    
        

    # now hop across the friend axis
    # + calculate min distance again and add it in

    if y - lj_end < 0:
        left_arc += min(lj_end - y, y - lj_end + 2*n)
    else:
        left_arc += min(y - lj_end, lj_end - y + 2*n)
    
    if y - rj_end < 0:
        right_arc += min(rj_end - y, y - rj_end + 2*n)
    else:
        right_arc += min(y - rj_end, rj_end - y + 2*n)

    print(min(naive, left_arc, right_arc))

