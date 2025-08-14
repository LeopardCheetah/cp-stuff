import sys

def count(ls, obj):
    x = 0
    for i in ls[0]:
        if i == obj:
            x += 1
    
    return x

for _ in range(int(sys.stdin.readline())):
    b, n = map(int, sys.stdin.readline().strip().split())
    
    # b - cost
    # n - number of buildings

    buildings = [int(a) for a in sys.stdin.readline().strip().split()]
    buildings.sort()


    # work backwards from max cost
    # naive

    s = sum(buildings)

    # lemma: at height h, cost - danger = s - h*n
    # so cost = danger + s - h*n at some point p
    # danger = cost + h*n - s

    cost_ls = [s] # height 0 has cost sum(b) 
    
    counter = n
    last_val = s
    cost_len = 0
    for i in range(n):
        # buildings[i] --> next thing
        if i == 0:
            pass
        else:
            if buildings[i] == buildings[i - 1]: # i = 0 works lmao
                continue

        for j in range(buildings[i] - cost_len):
            cost_ls.append(last_val - n + i)
            last_val -= n - i
        
        cost_len += (buildings[i] - cost_len)


    danger_ls = [cost_ls[some_cost_ind] - s + some_cost_ind*n for some_cost_ind in range(len(cost_ls))]


    dch = [(cost_ls[ind], danger_ls[ind], ind) for ind in range(len(cost_ls))]

    # find value
    # technically wrong code
    for cost_danger_set in dch:
        if cost_danger_set[0] > b:
            continue
        
        try:
            if (cost_danger_set[1]) == dch[cost_danger_set[2] + 1]:
                continue
        except:
            pass

        print(cost_danger_set[2])
        break

