# note: run this with pypy (or at least on idejudge run it with pypy so it doesnt tle)

lines = 2686 # way more than expected

# lava drops 
lava_drops = []
enc_lava_drops = [] # looks like max is 20 so encode with 10000x + 100y + z

for _ in range(lines):
    x, y, z = map(int, input().strip().split(','))

    lava_drops.append((x, y, z))
    enc_lava_drops.append(10000*x + 100*y + z)

enc_lava_drops.sort()


# corners of a 20x20x20 grid - these are all "outside" points
outside = [0, 20, 2000, 200000, 202020, 200020, 2020, 202000]

# 3d field flow search yay!!!!
def is_outside(v): # check if v is connected to the "outside"
    # e.g. there exists a path from v -> (0, 0, 0) or (20, 20, 20)
    # w/o crossing any squares in lava_drops/enc_lava_drops
    global outside
    global enc_lava_drops

    if v in outside:
        return True 
    
    if is_in(v): # in enc_lava_drops
        return False 
    
    points_visited = [v]
    flow_sqs = [v]

    while len(flow_sqs) > 0:
        flow = flow_sqs.pop()

        # look at next 6 squares, decide if we flow with them or not
        tentative_sqs = [flow + 10000, flow - 10000, flow + 100, flow - 100, flow + 1, flow - 1]
    
        for t in tentative_sqs:
            if is_in(t): # in enc lava drops.
                continue # pass .
            
            if t in points_visited:
                continue # still pass
            
            if t in outside:
                outside += points_visited
                return True 
            
            # still tentative, undecided
            points_visited.append(t)
            flow_sqs.append(t)
            continue 
        
        continue 
    
    # we did not make it out gang
    enc_lava_drops += points_visited
    enc_lava_drops.sort()
    return False 





def is_in(v):
    # is in enc_lava_drops?
    left = 0
    right = len(enc_lava_drops)

    while left < right:
        mid = (left + right) // 2
        if enc_lava_drops[mid] == v:
            return True 
        
        if enc_lava_drops[mid] < v:
            left = mid + 1
            continue 
        
        right = mid - 1
        # mid > v so move right bound down.
    
    if left > len(enc_lava_drops) - 1:
        return False 

    return enc_lava_drops[left] == v
    

c = 0
for d in enc_lava_drops:
    # just check +x/-x, +y/-y, +z/-z.



    tents = [d + 10000, d - 10000, d + 100, d - 100, d + 1, d - 1]
    for t in tents:
        c += is_outside(t)
    
    # 22482, too high.

print(c)

    