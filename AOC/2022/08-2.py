# 99 by 99 grid.
sq_length = 99

grid = []
for _ in range(sq_length):
    row = []

    trees = input().strip()
    for i in trees:
        row.append(int(i))
    
    grid.append(row)
    continue 

score = 0

for i in range(99):
    for j in range(99):
        if i == 0 or j == 0 or i == 98 or j == 98:
            continue # on the edge.

        # calculate score.
        w, a, s, d = 0, 0, 0, 0


        v = grid[i][j]

        for _a in range(i - 1, -1, -1):
            if v > grid[_a][j]:
                w += 1
                continue 

            if v <= grid[_a][j]:
                w += 1
                break
            
            

        for _a in range(i + 1, 99):
            if v > grid[_a][j]:
                s += 1
                continue 

            if v <= grid[_a][j]:
                s += 1
                break 
        
        for _b in range(j - 1, -1, -1):
            if v > grid[i][_b]:
                a += 1 
                continue 

            if v <= grid[i][_b]:
                a += 1 
                break

        for _b in range(j + 1, 99):
            if v > grid[i][_b]:
                d += 1
                continue
            
            if v <= grid[i][_b]:
                d += 1
                break
        
        _score = w*a*s*d
        score = max(_score, score)

        

print(score)