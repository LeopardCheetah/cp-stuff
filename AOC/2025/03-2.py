# not locked in today
# didnt start on time

lines = 200
c = 0

def find_largest(s):
    # returns largest char ('9' > '8' > ... > '1') and index.
    for digit in ['9', '8', '7', '6', '5', '4', '3', '2', '1']:
        if s.count(digit):
            ind = s.find(digit) # this is relative index.
            
            return digit, ind
    
    return '0', 'error!'

for _ in range(lines):
    i = input().strip()
    j = ''

    cuind = 0 # cumulative index sum
    n = '' # number.

    for it in range(12, 0, -1):
        # rub the first few chars and find the largest char.
        if it == 1:
            j = i[cuind:]
        else:
            j = i[cuind:-(it - 1)]
        _digit, index = find_largest(j)

        if index == 'error!':
            print(i)
            print(j)
            print(it)
            print(cuind)
            print(n)

        n += _digit 
        cuind += index + 1
    
    c += int(n)


            
        

print(c)