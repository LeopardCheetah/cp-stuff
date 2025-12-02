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

# unamortized, takes a bit.
def get_monkey(m):
    # get monkey with string m

    if type(monkey_db[m]) == type(3):
        return monkey_db[m] # int.
    
    # else its an operand 
    oper = monkey_db[m][4]
    f = monkey_db[m][:4]
    s = monkey_db[m][5:]
    if oper == '+':
        return get_monkey(f) + get_monkey(s)
    
    if oper == '*':
        return get_monkey(f) * get_monkey(s)
    
    if oper == '/':
        return get_monkey(f) // get_monkey(s)

    return get_monkey(f) - get_monkey(s)

print(get_monkey('root'))