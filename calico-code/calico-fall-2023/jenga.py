mod = 3359232

for _ in range(int(input())):
    tiles = int(input())

    n = pow(2, (tiles//3 + 1), mod)

    if n < 2:
        print(mod + n - 2)
        continue

    print(n - 2)