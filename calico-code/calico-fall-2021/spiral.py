def spiral(k):

    if k == 0:
        return ['@']

    # 4x + 1 by 4x + 1 grid


    # @@@@@
    #     @
    # @@@ @
    # @   @
    # @@@@@


    head = ['@']*(4*k + 1)
    two = [' ']*(4*k) + ['@']
    four = ['@'] + [' ']*(4*k - 1) + ['@']

    # traverse on spiral k-1

    ls = []

    imported_ls = spiral(k-1)

    # ls needs to be a one-dimensional list holding (4k-3) by (4k+1) - we then add the filler there
    
    for row in range(4*k - 3):
        ls += ['@', ' ']

        if row == 0:
            ls[1] = '@'
        
        ls += imported_ls[(4*k-3)*row:(4*k-3)*(row + 1)]
        # add first 4k - 3 characters from imported_ls

        ls += [' ', '@']


    return head + two + ls + four + head

def ans(k):
    ls = spiral(k)

    # now we make this into readable strings
    # break up at chunks

    s = ''

    # get in batches
    
    # 4k + 1 by 4k + 1

    for i in range(4*k + 1):
        s += ''.join(ls[(4*k + 1)*i:(4*k + 1)*(i + 1)]) + '\n'
    
    return s


for _ in range(int(input())):
    print(ans(int(input())))