for _ in range(int(input())):
    a, b = map(float, input().strip().split(':'))

    if a == 0:
        print("SAFE")
        continue

    if b/a <= 1:
        print("SWERVE")
        continue

    if b/a <= 5:
        print("BRAKE")
        continue

    print("SAFE")