for _ in range(int(input())):
    # bricks
    # count lol
    w, h, b, m = map(int, input().split())
    # w for width, h for height (num of new lines), b for num of bricks, m for num of bricks wanted
    # h more lines

    # since test cases are small we just win


    big_ls = []
    for i in range(h):
        ls = input().strip().split()

        for j in ls:
            big_ls.append(int(j))


    brick_counts = [0]*(b+1) # remember the 0th brick

    for n in big_ls:
        brick_counts[n] += 1
    
    brick_counts = brick_counts[1:]

    brick_counts.sort()

    s = 0
    for i in range(m):
        s += brick_counts[i]
    
    print(s)