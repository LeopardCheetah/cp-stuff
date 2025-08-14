for i in range(int(input())):
    n = int(input())

    if n == 0:
        print('haha good one')
        continue

    if n > 179:
        print('canceled')
        continue

    print('berkeley'*(n//10) + 'time')