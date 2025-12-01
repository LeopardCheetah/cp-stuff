# 2000 line input
instructions = 2000

# encode (x, y) as 10000x + y 
# this list might be super duper long.
tail_positions = [0]
x = [0]*10
y = [0]*10

for _ in range(instructions):
    d, n = input().strip().split()
    n = int(n)

    s = d*n
    for ch in s:
        # simulate head movement
        if ch == 'U':
            y[0] += 1
        if ch == 'L':
            x[0] -= 1
        if ch == 'R':
            x[0] += 1
        if ch == 'D':
            y[0] -= 1
        
        # from here move each digit off of that
        for knot_idx in range(1, 10):
            # check if touching 
            if max(x[knot_idx] - x[knot_idx - 1], x[knot_idx - 1] - x[knot_idx]) < 2:
                if max(y[knot_idx] - y[knot_idx - 1], y[knot_idx - 1] - y[knot_idx]) < 2:
                    continue 
            
            # not touching.
            # move to catch up
            dx = x[knot_idx - 1] - x[knot_idx]
            dy = y[knot_idx - 1] - y[knot_idx]

            if dx > 0:
                x[knot_idx] += 1 
            if dx < 0:
                x[knot_idx] -= 1
                
            if dy > 0:
                y[knot_idx] += 1
            if dy < 0:
                y[knot_idx] -= 1
        
        tail_positions.append(10000*x[-1] + y[-1])
    
print(len(tail_positions))
print(len(set(tail_positions)))