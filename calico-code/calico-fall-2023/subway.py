for _ in range(int(input())):
    passenger, station, capacity = map(int, input().split())

    start = [int(a) for a in input().split()]
    end = [int(a) for a in input().split()]

    if capacity >= passenger:
        print(max(end) - 1)
        continue


    # passengers > capacity
    # idea: kick passengers forward

    passengers = [(start[i], end[i]) for i in range(len(start))]
    passengers.sort() # queue like structure or something
    

    # idea!! load up first few passengers like in a queue, and drop those that can be dropped and so on
    # drop = get popped 
    # this is a scheduling problem?????
    

    

