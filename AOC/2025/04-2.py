# started at 10:43 pst

# 139 x 139 grid
lines = 139

grid = []

for _ in range(lines):
    grid.append(list(input().strip()))


def get(i, j):
    if i < 0 or j < 0:
        return 0
    
    if i > lines - 1 or j > lines - 1:
        return 0
    
    return grid[i][j] == '@'

it = 0
count = 0
c = 1
while c:
    c = 0
    remove = []
    for row in range(lines):
        for col in range(lines):
            if not get(row, col):
                continue 

            d = 0
            
            tents = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
            for p in tents:
                d += get(row + p[0], col + p[1])
            
            if d < 4:
                c += 1
                remove.append((row, col))


    count += c 
    
    for pair in remove:
        grid[pair[0]][pair[1]] = '.'
    
    print(c, remove, count)

print(count)