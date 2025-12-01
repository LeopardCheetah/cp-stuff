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

# just iterate over every item and add it all up
c = 0

for i in range(99):
    for j in range(99):
        if i == 0 or j == 0 or i == 98 or j == 98:
            c += 1
            continue # on the edge.

        # check from the top
        top, left, right, bottom = False, False, False, False 

        v = grid[i][j]

        for a in range(i - 1, -1, -1):
            if v <= grid[a][j]:
                top = True 
                break

        for a in range(i + 1, 99):
            if v <= grid[a][j]:
                bottom = True 
                break
        
        for b in range(j - 1, -1, -1):
            if v <= grid[i][b]:
                left = True 
                break

        for b in range(j + 1, 99):
            if v <= grid[i][b]:
                right = True 
                break

        c += 1 - (top and left and right and bottom)

print(c)