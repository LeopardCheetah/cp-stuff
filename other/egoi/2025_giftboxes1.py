# 2025 EGOI
# Day 1
# A. Gift Boxes

# 2s, 1gb
# 25/100
# O(n^2) so tle ac ac tle tle tle

t, n = map(int, input().split())
ls = [int(a) for a in input().split()] # len(ls) = n


# we must remove at least n - t people from the lineup
# lowkey naive algorithm going on here
optimal_left, optimal_right, optimal_removed = 0, 0, n

# minimize optimal_removed
# i objects (at LEAST) need to be removed
for i in range(n - t, n):
    if optimal_removed <= i:
        # no better sol 
        break
    
    oleft, oright = 0, 0
    oremoved = optimal_removed

    # try to remove i elements via sliding window and see how it goes i guess
    for j in range(n - i + 1):
        # j indices to try this out on
        # hella time complexity going on here

        if len(set(ls[:j] + ls[i + j:])) == n - i:
            # we have a winner!!!
            optimal_left = j
            optimal_right = i + j - 1
            optimal_removed = i
            break

    # if optimal_removed - oremoved:
    #     optimal_left, optimal_right = oleft, oright
    #     optimal_removed = oremoved


print(optimal_left, optimal_right, optimal_removed)
    


