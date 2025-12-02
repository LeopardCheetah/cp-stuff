# this one was solved mor eby trial and error than reverse engineering or whatever.
# lol 
# binary searched kinda manually (with the range of 1000) for the exact value i needed to make both sides equal
# helps that (for me) when humn++, the thing that i wanted to control went down almost linearly.


lines = 2037 # thats a lot

# parse it
monkey_db = {}
for _ in range(lines):
    i = input().strip().split()

    if len(i) == 2: 
        # monkey shouts out number
        monkey_db[i[0][:4]] = int(i[1])
        continue 
    
    # monkey shouts out an operand
    monkey_db[i[0][:4]] = i[1] + i[2] + i[3] # should be 9 chars long

def get_monkey(m):
    # get monkey with string m

    if type(monkey_db[m]) == type(3):
        return monkey_db[m] # int.
    
    # else its an operand 
    oper = monkey_db[m][4]
    f = monkey_db[m][:4]
    s = monkey_db[m][5:]
    _f = get_monkey(f)
    _s = get_monkey(s)

    # monkey_db[f] = _f 
    # monkey_db[s] = _s 

    if oper == '+':
        return _f + _s
    
    if oper == '*':
        return _f * _s
    
    if oper == '/':
        if _f % _s:
            print('fail')
            return 0
            
        return _f // _s 

    return _f - _s 


# 49160133593649 3509819803065
# 49160133593649 3509819803066
# 49160133593649 3509819803067
# 49160133593649 3509819803068
# 49160133593649 3509819803069
# 49160133593649 3509819803070

lower = 3509819802500
for i in range(lower, lower + 1000):
    monkey_db['humn'] = i 
    print(get_monkey('rcsj'), i)
    
# so find h such that get_monkey('rcsj') = 49160133593649

# 92974416424981
# 49160133593649

# print(get_monkey('rcsj')) # human required, 110431559233905
# print(get_monkey('zfsf')) # 49160133593649