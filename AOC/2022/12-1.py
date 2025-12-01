ins = 41
cols = 159

grid = []
for _ in range(ins):
    grid.append(list(input().strip()))

# just do some field flow bfs stuff
c = 0
seen = [20000] # (r, c) => 1000r + c

flow = [(20, 0)]

found = False 

while not found:
    if c > 10**7:
        print(seen, flow)
        print('RLE!!!')
        break

    c += 1
    _flow = []

    for pair in flow:
        # explore each direction
        tents = []

        if pair[0] != 0:
            tents.append((pair[0] - 1, pair[1]))
        if pair[0] != ins - 1:
            tents.append((pair[0] + 1, pair[1]))
        if pair[1] != 0:
            tents.append((pair[0], pair[1] - 1))
        if pair[1] != cols - 1:
            tents.append((pair[0], pair[1] + 1))


        if grid[pair[0]][pair[1]] in ['y', 'z']:
            for _pair in tents:
                if grid[_pair[0]][_pair[1]] == 'E':
                    found = True 
                    print(f'FOUND!!! Answer: {c}')
                    break
        
        v = grid[pair[0]][pair[1]]
        if v == 'S':
            v = 'a'

        for _pair in tents:
            if ord(grid[_pair[0]][_pair[1]]) > ord(v) + 1:
                continue # can't step too high
            
            if 1000*_pair[0] + _pair[1] in seen:
                # well it's seen
                continue 

            _flow.append(_pair)
            seen.append(1000*_pair[0] + _pair[1])
    
    flow = _flow
    
print(f'Answer: {c}')