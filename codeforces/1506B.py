import sys

for _ in range (int(sys.stdin.readline())):
    l, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()

    # O(n)?
    # look ahead and see if you can take the maximum greedy position and replace that with a "x"

    c = s.find('*') # str ind
    e = 0

    for i in range(len(s)):
        # s - c - 1
        if s[l - i - 1] == '*':
            e = l - i - 1
            break
    
    # check 1
    if c == e:
        print(1)
        continue

    co = 2

    # wlog problem is right so if we cant find a asterisk in the next few we quit
    f = True
    while f:
        if c == e:
            f = False
            co -= 1
            continue
            # reached the end

        if c + k + 1 >= l:
            f = False 
            continue # we've reached the end
        
        co += 1
        # find next '*'
        # greed it out
        for i in range(k, 0, -1):
            if s[c + i] == '*':
                c += i
                break
    
    print(co)