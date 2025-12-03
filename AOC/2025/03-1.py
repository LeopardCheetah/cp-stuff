# not locked in today
# didnt start on time

lines = 200
c = 0

for _ in range(lines):
    i = input().strip()

    j = i[:-1]

    # match to highest char then just look for next highest char from then onwards.
    highest_char = '0'
    for digit in ['9', '8', '7', '6', '5', '4', '3', '2', '1']:
        if j.count(digit):
            ind = i.find(digit)
            h = i[ind + 1:]
            

            for digit2 in ['9', '8', '7', '6', '5', '4', '3', '2', '1']:
                if digit < digit2 and digit2 != i[-1]:
                    continue # ehrm what
                
                if h.count(digit2):
                    c += int(digit + digit2)
                    break
            
            break
        
        continue 
    

            
        

print(c)