cases = 150



def subcompare(l, r):
    # can return either True, True or True, False or False, False 
    # TT => T
    # TF => F
    # FF => indeterminate
    # FT => NO.

    _l = 0
    _r = 0
    

    if type(l) == type(2):
        _l = [l]
    else:
        _l = l[:]
    
    if type(r) == type(4):
        _r = [r]
    else:
        _r = r[:]


    if not len(_l) and not len(_r):
        return False, False 
    
    if len(_l) == 0 and len(_r):
        return True, True

    if len(_r) == 0 and len(_l):
        return True, False 


    if type(_l[0]) == type(_r[0]) == type(0):
        # both are ints, check 
        if _l[0] < _r[0]:
            return True, True 
        
        if _l[0] > _r[0]:
            return True, False 
        
        _l.pop(0)
        _r.pop(0)

        return subcompare(_l, _r)
  

    if type(_l[0]) == type(_r[0]) == type([]):
        # list to list comparison
        # check first to make sure whats going on
        if len(_l[0]) == len(_r[0]):
            for ind, val in enumerate(_l[0]):

                # what if val is a list? what if _r[0][ind] is a list?
                # subcompare i guess

                _o, _t = subcompare(val, _r[0][ind])
                if _o:
                    return _o, _t 
                
                # indeterminate result. move on to the next one.    
                continue 
            
            # so all values are equal too
            _l.pop(0)
            _r.pop(0)
            return subcompare(_l, _r)
        
        # lengths differ
        # we should be ok to just do a compare on l/r => ints and we should be done; this WILL return a value.
        return subcompare(_l[0], _r[0])

    
    # types differ.
    if type(_l[0]) == type(3):
        _l[0] = [_l[0]]
        return subcompare(_l, _r)
    
    _r[0] = [_r[0]]
    return subcompare(_l, _r)
    


def compare(l, r):
    _l = 0
    _r = 0

    if type(l) == type(2):
        _l = [l]
    else:
        _l = l[:]
    
    if type(r) == type(4):
        _r = [r] 
    else:
        _r = r[:]


    # return true/false if l < r
    if len(_l) == 0 and len(_r):
        return True 

    if len(_r) == 0 and len(_l):
        return False 

    if type(_l[0]) == type(_r[0]) == type(0):
        # both are ints, check 
        if _l[0] < _r[0]:
            return True 
        
        if _l[0] > _r[0]:
            return False 
        
        _l.pop(0)
        _r.pop(0)

        return compare(_l, _r)
    
    if type(_l[0]) == type(_r[0]) == type([]):
        # list to list comparison
        # check first to make sure whats going on

        _one, _two = subcompare(_l[0], _r[0])
        if _one:
            return _two
        
        _l.pop(0)
        _r.pop(0)

        return compare(_l, _r)

    # types differ.
    if type(_l[0]) == type(3):
        _l[0] = [_l[0]]
        return compare(_l, _r)
    
    _r[0] = [_r[0]]
    return compare(_l, _r)

big_list = []


for i in range(cases):
    # just kidding we dont care about indices anymore

    # thank goodness for python eval
    a = eval(input().strip())
    b = eval(input().strip())
    _ = input()

    big_list.append(a)
    big_list.append(b)


# apply a sorting algorithm on big_list with the sorting algorithm in question being the compare() function
# use a stupid sort
# insertion sort??? who knows
print(big_list)

big_list.append([[2]])
big_list.append([[6]])
n = len(big_list)

ind = 1 
while ind < n:

    sind = ind - 1

    while sind > -1:
        if not compare(big_list[sind], big_list[sind + 1]):
            # must do a swap here.
            big_list[sind], big_list[sind + 1] = big_list[sind + 1], big_list[sind]
            sind -= 1
            continue 
        
        break # we're good
    
    ind += 1

# done!
print(big_list)
print((big_list.index([[2]]) + 1)*(big_list.index([[6]]) + 1))

"""
insertion sort alg:

i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while
"""