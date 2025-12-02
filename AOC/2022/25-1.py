lines = 125

# 2, 1, 0, - , =
def snafu_to_int(s):
    a = 0
    p = 0

    _map = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
    
    for ch in s[::-1]:
        a += _map[ch]*(5**p)
        p += 1
        continue 
    
    return a

def int_to_snafu(i):
    # replace "4" with 1-, 3 with 1=, 2 with 2, 1 with 1, 0 with 0
    # something something string addition needed here.

    # turn to base 5 then convert the number from there.

    b = ''
    j = i
    while j > 0:
        digit = j % 5 
        j = j // 5 
        b = b + str(digit)
    
    # b should be in base 5 now (but bakcwards)
    # convert!

    _door = ['2', '1', '0', '-', '=']

    _snaf = ''
    carry = False 
    for ch in b:
        if ch in ['0', '1', '2']:
            if carry:
                # leading 1
                carry = False
                if ch == '0':
                    _snaf = '1' + _snaf[1:]
                    continue 
                
                if ch == '1':
                    _snaf = '2' + _snaf[1:]
                    continue 
                
                carry = True 
                _snaf = '1=' + _snaf[1:] # 2 + 1 = 3
                continue 
            
            carry = False
            # no carry, just append
            _snaf = ch + _snaf 
            continue
    
        # 
        if ch == '3':
            if not carry:
                _snaf = '1=' + _snaf 
                carry = True 
                continue 
            
            # carry is true; leading 1 
            _snaf = '1-' + _snaf[1:]
            carry = True 
            continue 
        
        # ch == 4
        if not carry:
            _snaf = '1-' + _snaf 
            carry = True 
            continue 

        _snaf = '10' + _snaf[1:]
        carry = True 
        continue 

    return _snaf            


s = 0

for i in range(lines):
    s += snafu_to_int(input().strip())

print(int_to_snafu(s))