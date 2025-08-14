for i in range(int(input())):
    if i != 0:
        blank_line = input()

    absent, l = input().strip().split()

    names_list = [absent]
    returned_books = []

    for j in range(int(l)):
        k = input().strip().split()
        # k[0], k[3]

        names_list.append(k[0])
        returned_books.append(k[3][:len(k[3]) - 2])
    
    
    # slow version
    name = ''

    for q in names_list:
        if q not in returned_books:
            name = q
            break
    
    print(absent, "HAS", name+"'s BOOK")