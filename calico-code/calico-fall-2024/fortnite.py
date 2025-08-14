import sys

def count(ls, obj):
    x = 0
    for i in ls[0]:
        if i == obj:
            x += 1
    
    return x

for _ in range(int(sys.stdin.readline())):
    n, h, d, s, p = map(int, sys.stdin.readline().strip().split())

    # n -- starting health
    # h -- heal/s (+)
    # d -- distance to go
    # s -- running speed
    # p -- dmg/s (-)

    if n >= (d/s)*p:
        print(d/s)
        continue
    
    if h - p <= 0:
        print(-1)
        continue

    # rack up health for p seconds then win

    extra_health = d*p/s - n 

    print(d/s + extra_health/(h - p))    