# 2025 EGOI
# Day 1
# A. Gift Boxes

# 2s, 1gb


# idea: (unfinished as hell)
# figure out where 1st, 2nd, 2nd to last, last indices are for each number
# then from there 'normalize'
# then find the best configs of covering either the 1-3 range or 2-4 range and see 
# what the minimum amount of squares needed to satisfy all the numbers are

# but that's the hard part





t, n = map(int, input().split())
ls = [int(a) for a in input().split()] # len(ls) = n

one = [0]*t 
two = [0]*t 
three = [0]*t 
four = [0]*t

for i, v in enumerate(ls):
    if four[v]:
        three[v] = four[v]
        four[v] = i 
        continue 
    
    if three[v]:
        four[v] = i 
        continue 

    if two[v]:
        three[v] = i 
        continue 
    
    if one[v]:
        two[v] = i 
        continue 
    
    one[v] = i + 1

for i, v in enumerate(one):
    one[i] = v - 1

print(one)
print(two)
print(three)
print(four)

