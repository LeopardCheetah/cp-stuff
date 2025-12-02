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
            if len(str(k)) % 2 == 0:
                # check halves
                fhalf = str(k)[:len(str(k)) // 2]
                shalf = str(k)[len(str(k)) // 2:]



                if fhalf == shalf:
                    c += k 
                    continue 
            
            # check x 3
            if len(str(k)) % 3 == 0:
                parts = [str(k)[:len(str(k)) // 3], str(k)[len(str(k)) // 3:2*(len(str(k)) // 3)], str(k)[2*(len(str(k)) // 3):]]
                
                if parts[0] == parts[1] == parts[2]:
                    c += k 
                    continue 

            # longest is tens
            # so check 3x, 5x, 7x


            # check x7
            if k in [1111111*ind for ind in range(1, 10)]:
                c += k
                continue 

            # check x5
            # would be two digit thing repeated over and over

            if k in [11111*ind for ind in range(1, 10)]:
                c += k
                continue 

            p = k
            first = p % 100
            p = p // 100
            second = p % 100
            p = p // 100
            thi = p % 100
            p = p // 100
            fo = p % 100
            p = p // 100
            fif = p % 100

            if first == second == thi == fo == fif:
                c += k
                continue 




print(c)

