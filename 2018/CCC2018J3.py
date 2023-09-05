DList = input("")
D = DList.split()
StartCity = 1

if StartCity == 1:
    print("0", end='',) 
    print(" ", end='')
    print(0+int(D[0]), end='',  )
    print(" ", end='')
    print(0+int(D[0])+int(D[1]), end='',  )
    print(" ", end='')
    print(0+int(D[0])+int(D[1])+int(D[2]), end='',  )
    print(" ", end='')
    print(0+int(D[0])+int(D[1])+int(D[2])+int(D[3]), end='',  )
    print("")
    StartCity += 1

if StartCity == 2:
    print(0+int(D[0]), end='')
    print(" ", end='')
    print("0", end='')
    print(" ", end='')
    print(0+int(D[1]), end='')
    print(" ", end='')
    print(0+int(D[1])+int(D[2]), end='')
    print(" ", end='')
    print(0+int(D[1])+int(D[2])+int(D[3]), end='')
    print("")
    StartCity += 1

if StartCity == 3:
    print(0+int(D[0])+int(D[1]), end='')
    print(" ", end='')
    print(0+int(D[1]), end='')
    print(" ", end='')
    print("0", end='')
    print(" ", end='')
    print(0+int(D[2]), end='')
    print(" ", end='')
    print(0+int(D[2])+int(D[3]), end='')
    print("")
    StartCity += 1

if StartCity == 4:
    print(0+int(D[0])+int(D[1])+int(D[2]), end='')
    print(" ", end='')
    print(0+int(D[1])+int(D[2]), end='')
    print(" ", end='')
    print(0+int(D[2]), end='')
    print(" ", end='')
    print("0", end='')
    print(" ", end='')
    print(0+int(D[3]), end='')
    print("")
    StartCity += 1

if StartCity == 5:
    print(0+int(D[0])+int(D[1])+int(D[2])+int(D[3]), end='')
    print(" ", end='')
    print(0+int(D[1])+int(D[2])+int(D[3]), end='')
    print(" ", end='')
    print(0+int(D[2])+int(D[3]), end='')
    print(" ", end='')
    print(0+int(D[3]), end='')
    print(" ", end='')
    print("0", end='')
    StartCity += 1