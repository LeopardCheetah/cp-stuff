cases = 150

s = 0


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



for i in range(cases):
    j = i + 1 # actual index we care about.

    # thank goodness for python eval
    left = eval(input().strip())
    right = eval(input().strip())
    _ = input()

    s += j*compare(left, right)

print(s)

    