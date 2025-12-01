# 138
instructions = 138


cycle = 0
sprx = 1

for _ in range(instructions):
    _in = input().strip()

    if _in == 'noop':
        if sprx - 1 == cycle or sprx == cycle or sprx + 1 == cycle:
            print('#', end='')
        else:
            print(' ', end='')
        
        cycle += 1
        if cycle == 40:
            cycle = 0
            print()

        continue 
    

    _add = int(_in.split()[1])
    if sprx - 1 == cycle or sprx == cycle or sprx + 1 == cycle:
        print('#', end='')
    else:
        print(' ', end='')
        
    cycle += 1
    if cycle == 40:
        cycle = 0
        print()
    
    if sprx - 1 == cycle or sprx == cycle or sprx + 1 == cycle:
        print('#', end='')
    else:
        print(' ', end='')
        
    cycle += 1
    if cycle == 40:
        cycle = 0
        print()
    
    sprx += _add 


            