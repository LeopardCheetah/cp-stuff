# implementation problem

import sys

for _ in range(int(sys.stdin.readline())):
    q, n, m = map(int, sys.stdin.readline().split())

    # q actions
    # n roles
    # m people

    # use a number to encode people's roles
    # use and to get it out

    pings = [0]*m
    roles = [[] for i in range(m)]


    for i in range(q):
        query = sys.stdin.readline().strip().split()

        if query[0] == 'A':
            # A [role] [user]
            roles[int(query[2]) - 1].append(int(query[1]))
            continue

        if query[0] == 'R':
            # R [role] [user]
            roles[int(query[2]) - 1].pop(roles[int(query[2]) - 1].index(int(query[1])))
            continue
            
        # P [role]
        # figure out who has this role
        for k in range(m):
            if int(query[1]) in roles[k]:
                pings[k] += 1


    for item in range(m):
        pings[item] = str(pings[item])

    print(' '.join(pings))

