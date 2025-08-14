# i dont expect this to work

import sys

for _ in range(int(sys.stdin.readline())):
    l1, l2 = map(int, sys.stdin.readline().split())
    ls = [a for a in sys.stdin.readline().strip().split()]
    lst = [b for b in sys.stdin.readline().strip().split()]
    lsf = ls + lst
    lsf.sort()
    print(' '.join(lsf))
