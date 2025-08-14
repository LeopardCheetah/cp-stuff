# constaints say a_n <= 10^3 so
# 1 <= x <= 10^3

import sys

for _ in range(int(sys.stdin.readline())):
    l = int(sys.stdin.readline())
    ls = [0]*(10**3 + 1)

    ls[0] = -1 # checker

    # update
    inp = [int(a) for a in sys.stdin.readline().split()]

    for num in inp:
        ls[num] += num
    
    print(ls.index(max(ls)))


