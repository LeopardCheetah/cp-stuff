lines = 2686 # way more than expected

# lava drops 
lava_drops = []
enc_lava_drops = [] # looks like max is 20 so encode with 10000x + 100y + z

for _ in range(lines):
    x, y, z = map(int, input().strip().split(','))

    lava_drops.append((x, y, z))
    enc_lava_drops.append(10000*x + 100*y + z)

enc_lava_drops.sort()

def is_in(v):
    # is in enc_lava_drops?
    left = 0
    right = len(enc_lava_drops)

    while left < right:
        mid = (left + right) // 2
        if enc_lava_drops[mid] == v:
            return True 
        
        if enc_lava_drops[mid] < v:
            left = mid + 1
            continue 
        
        right = mid - 1
        # mid > v so move right bound down.
    
    if left > len(enc_lava_drops) - 1:
        return False 
        
    return enc_lava_drops[left] == v
    

c = 0
for d in enc_lava_drops:
    # just check +x/-x, +y/-y, +z/-z.

    c += 6


    tents = [d + 10000, d - 10000, d + 100, d - 100, d + 1, d - 1]
    for t in tents:
        c -= is_in(t)
    

print(c)

    