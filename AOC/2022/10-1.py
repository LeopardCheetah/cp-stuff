# 138
instructions = 138

magic_cycles = [20, 60, 100, 140, 180, 220]
cycle = 0
x = 1
s = 0

for _ in range(instructions):
    _in = input().strip()

    if _in == 'noop':
        cycle += 1
        if cycle in magic_cycles:
            s += x*cycle 
        
        continue 
    

    _add = int(_in.split()[1])
    cycle += 1
    if cycle in magic_cycles:
        s += x*cycle 
    
    cycle += 1
    if cycle in magic_cycles:
        s += x*cycle 
    
    x += _add 

print(s)
            