with open('in.txt', 'r') as i, open('out.txt', 'w') as w:
    x = i.readline()
    x = i.readline()


    for ind in range(18136):
        a, b = map(int, i.readline().split())
        w.write(str(b - 1) + ', ')

