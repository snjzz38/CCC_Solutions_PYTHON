Matrix = []
N = int(input(""))
K = N-1
Target = [[0 for _ in range(N)] for _ in range(N)]

def CW90():
    global Target
    for i in range(N):
        for j in range(N):
            Target[j][K-i] = Matrix[i][j]

def CCW90():
    global Target
    for i in range(N):
        for j in range(N):
            Target[K-j][i] = Matrix[i][j]

def CW180():
    global Target
    for i in range(N):
        for j in range(N):
            Target[K-i][K-j] = Matrix[i][j]

def printMatrix(M):
    global N
    for i in range(N):
        for j in range(N):
            print(M[i][j], end='')
            print(" ", end='')
        print("")

for i in range(N):
    Table = input("")
    Matrix.append(Table.split())

List = []
List.append(int(Matrix[0][0]))
List.append(int(Matrix[0][N-1]))
List.append(int(Matrix[N-1][0]))
List.append(int(Matrix[N-1][N-1]))


if int(Matrix[N-1][N-1]) == max(List):
    printMatrix(Matrix)
elif int(Matrix[0][N-1]) == max(List):
    CW90()
    printMatrix(Target)
elif int(Matrix[N-1][0]) == max(List):
    CCW90()
    printMatrix(Target)
elif int(Matrix[0][0]) == max(List):
    CW180()
    printMatrix(Target)





