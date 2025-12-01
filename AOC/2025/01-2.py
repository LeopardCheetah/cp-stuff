instructions = 4147

d = 50
c = 0

for _ in range(instructions):
    i = input().strip()
    a = int(i[1:])

    # my cpu is quick
    if i[0] == 'L':
        for b in range(a):
            d -= 1
            if not d % 100:
                c += 1

    else:
        for b in range(a):
            d += 1
            if not d % 100:
                c += 1


print(c)