N = int(input(""))
Distance = input("").split()
ListDistance = [0]

for i in range(len(Distance)):
    ListDistance.append(int(Distance[i]))

for i in range(N-1):
    ListDistance[i+1] = ListDistance[i]+ListDistance[i+1]
    print(ListDistance[i], end='')
    print(", ", end='')
print(ListDistance[N-1])

for i in range(N-1):
    for j in range(N):
        ListDistance[j] = ListDistance[j] - int(Distance[i])
        if ListDistance[j] < 0:
            print(ListDistance[j] * -1, end='')
            print(", ", end='')
        else:
            print(ListDistance[j], end='', sep=', ')
            if j < N-1:
                print(", ", end='')
    print("")
