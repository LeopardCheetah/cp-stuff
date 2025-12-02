lines = 1

ls = []
c = 0
for _ in range(lines):
    i = input().strip().split(',')

    for j in i:
        a, b = j.split('-')
        a = int(a)
        b = int(b)

        ls.append((a, b))

        for k in range(a, b + 1):
            if len(str(k)) % 2:
                continue 
            
            fhalf = str(k)[:len(str(k)) // 2]
            shalf = str(k)[len(str(k)) // 2:]



            if fhalf == shalf:
                c += k 
                print(k)




print(c)

