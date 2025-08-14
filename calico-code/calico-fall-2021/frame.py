
for i in range(int(input())):
    if i != 0:
        print()
    words = input().strip().split()

    m = len(words[0])
    for word in words:
        m = max(len(word), m)
    
    # asterisk lines
    # word lines
    # other

    print('*'*(m + 2))
    
    for word in words:
        print('*'+word + ' '*(m-len(word))+'*')
    
    print('*'*(m + 2))
