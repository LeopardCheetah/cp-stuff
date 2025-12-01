# 2000 line input
instructions = 2000

# encode (x, y) as 10000x + y 
# this list might be super duper long.
tail_positions = [0]
hx = 0
hy = 0
tx = 0
ty = 0

for _ in range(instructions):
    d, n = input().strip().split()
    n = int(n)

    s = d*n
    for ch in s:
        # simulate head movement
        if ch == 'U':
            hy += 1
        if ch == 'L':
            hx -= 1
        if ch == 'R':
            hx += 1
        if ch == 'D':
            hy -= 1
        
        # check if touching
        if max(hx - tx, tx - hx) < 2 and max(hy - ty, ty - hy) < 2:
            continue # nothing happened; no need to append
        
        # move tail to catch up
        dx = hx - tx 
        dy = hy - ty


        if dx > 0:
            tx += 1 
        if dx < 0:
            tx -= 1
            
        if dy > 0:
            ty += 1
        if dy < 0:
            ty -= 1
        
        tail_positions.append(10000*tx + ty)
    
print(len(tail_positions))
print(len(set(tail_positions))) # this is the actual answer