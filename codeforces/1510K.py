# archived this one since
# i use both a package(!!)
# and a main function to run things
# pretty innovative imo


import copy
def main():
    n = int(input())
    ls = [int(a) for a in input().split()]
    lst = [a for a in ls]

    # do a basic check to make sure problem is solvable
    f = True 
    for i in range(n):
        if ls[i] + ls[2*n - 1 - i] != 2*n + 1:
            f = False 
            break

    if not f:
        print(-1)
        return 
    
    solved = [a + 1 for a in range(n*2)]


    # still might not be solvable
    c = 0

    f = True 
    g = True 
        
    # apply operations over and over
    seen = []
    while f or g:

        if ls == solved or lst == solved:
            print(c)
            return
        
        if ls in seen and f:
            f = False 
            continue 
        
        if lst in seen and g:
            g = False 
            continue

        c += 1
        deep = copy.deepcopy(ls)
        seen.append(deep)
        deep = copy.deepcopy(lst)
        seen.append(deep)

        if c % 2:
            # swap ls 1, invert lst
            if g:
                lst = lst[n:] + lst[:n]

            if f:
                for ind in range(n):
                    ls[2*ind], ls[2*ind + 1] = ls[2*ind + 1], ls[2*ind]

            continue 
        
        if f:
            ls = ls[n:] + ls[:n]
        
        if g:
            for ind in range(n):
                lst[2*ind], lst[2*ind + 1] = lst[2*ind + 1], lst[2*ind]

        continue 

    print(-1)
    return




if __name__ == '__main__':
    main()