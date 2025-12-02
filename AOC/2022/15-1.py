lines = 23

coverage_areas = []

for _ in range(lines):
    i = input().split()


    sx = int(i[2][2:-1])
    sy = int(i[3][2:-1])

    bx = int(i[8][2:-1])
    by = int(i[9][2:])

    md = max(sx - bx, bx - sx) + max(sy - by, by - sy)
    # calculate md from that point to 2000000

    xd = md - max(2000000 - sy, sy - 2000000)
    if xd < 0:
        continue # not even worth it.

    # section off
    coverage_areas.append((sx - xd, sx + xd))

coverage_areas.sort()
print(coverage_areas)
# i looked manually from here
# lowkey think the answer is wrong but wtv
# should be max - min + 1 not just max - min.