def find(card_num, length):

    if length == 1:
        return 0
    
    if length == 2 and card_num == 1:
        return 1
    
    if length == 2:
        return 0

    if length % 2 == 0:
        if card_num % 2 == 0:
            return card_num // 2 - 1
        
        return length // 2 + find((card_num + 1)//2, length//2)
    
    if card_num % 2 == 0:
        return card_num // 2 - 1
    
    if card_num == 1:
        return length // 2 
    
    return length // 2 + 1 + find((card_num - 1)//2, length//2)


for i in range(int(input())):
    n, k = map(int, input().split())

    print(find(k, n) + 1)


# testing
'''
def shuffle(x):
    ls = [i + 1 for i in range(x)]


    for i in range(1, x):
        ls.append(ls.pop(i - 1))
    
    return ls

def shuff(ls):
    n = len(ls)
    lst = ls.copy()
    for i in range(1, n):
        lst.append(lst.pop(i - 1))

    return lst

def conv(ls):
    lst = ls.copy()
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    
    return lst

def mock_shuff(x):
    s = ' '
    # for i in range(x//2):
    #     s += str(2*(i + 1)) + '  '
    
    s += '  '.join(conv(shuff([2*n + 1 for n in range((x+1)//2)])))
    
    return s


print(shuffle(19))
print(shuffle(9))

print(shuffle(21))
print(shuffle(10))


# for even number of cards in shuffle
# even numbers = num/2 - 1
# odd numbers = index of 2n + 1 if you shuffle all the odd numbers from 1 to 2n - 1


# finds position of card using array indexing
def find(card_num, length):

    if length == 1:
        return 0
    
    if length == 2 and card_num == 1:
        return 1
    
    if length == 2:
        return 0

    if length % 2 == 0:
        if card_num % 2 == 0:
            return card_num // 2 - 1
        
        return length // 2 + find((card_num + 1)//2, length//2)
    
    if card_num % 2 == 0:
        return card_num // 2 - 1
    
    if card_num == 1:
        return length // 2 
    
    return length // 2 + 1 + find((card_num - 1)//2, length//2)

print(find(6666, 999))

'''