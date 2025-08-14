for _ in range(int(input())):

    # if 1st birthday is on day 1
    # nth birthday is on n^2 - n + 1 day of the year

    k = int(input())

    if k == 1:
        print('0')
        continue

    if k == 2:
        print('3')
        continue

    print(k**2 - k + (k*(k-1)*(2*k - 1))//6)