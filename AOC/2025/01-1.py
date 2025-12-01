instructions = 4147

d = 50
c = 0

for _ in range(instructions):
    i = input().strip()
    if i[0] == 'L':
        d -= int(i[1:])
    else:
        d += int(i[1:])
    
    if not d % 100:
        c += 1

print(c)