##########################################################
#####  WARNING - this sol is not completely correct  #####
##########################################################

# # this sol is not correct (part 2)
# for some reason it outputs 161523 and 160566 as the biggest numbers
# when they should be (161523, 160567)
# weird one-off error.



# gonna manually parse some stuff

# 0 -> operation
# # sq = sq, pos => new = old*x, neg => new = old + x
# 1 -> div test
# 2 -> if div test true 
# 3 -> if div test false
monkeys = [
    [19, 17, 4, 7],
    [11, 3, 3, 2],
    [-6, 19, 0, 4],
    [-5, 7, 2, 0],
    [-7, 2, 7, 5],
    ['s', 5, 1, 6],
    [-2, 11, 3, 1],
    [-3, 13, 5, 6]
]

items = [
    [72, 64, 51, 57, 93, 97, 68],
    [62], 
    [57, 94, 69, 79, 72],
    [80, 64, 92, 93, 64, 56],
    [70, 88, 95, 99, 78, 72, 65, 94],
    [57, 95, 81, 61],
    [79, 99],
    [69, 98, 62]
]

c = [0]*8

rounds = 10000
for r in range(rounds):
    if not r % 1000:
        print(c)
    # go thru each monkey and do stuff
    for m in range(8):
        c[m] += len(items[m])
        for i in items[m]:
            _i = i
            # apply operation
            # div worry mod
            # send to next monkey
            
            if monkeys[m][0] == 's':
                _i = _i*_i 
            elif monkeys[m][0] > 0:
                _i = _i*monkeys[m][0]
            else:
                _i = _i - monkeys[m][0]
            
            _i = _i % (17*3*19*7*2*5*11*13)

            if _i % monkeys[m][1]:
                # false
                items[monkeys[m][3]].append(_i)
                continue 
            
            items[monkeys[m][2]].append(_i)
            continue 
        
        items[m] = []

print(items)
print()

print(c) # multiply the two biggest numbers here
print(sum(c))
print()

max1 = max(c)
print(max1)
c.pop(c.index(max(c)))
max2 = max(c)
print(max2)
print(max1*max2)