size = 4
MatrixRow = []
MatrixCol = [[0 for _ in range(size)] for _ in range(size)]
FlagRow = False
FlagCol = False

for i in range(size):
    Row = input("").split()
    for j in range(size):
        Row[j] = int(Row[j])
    MatrixRow.append(Row)   

for i in range(size):
    for j in range(size):
        MatrixCol[j][i] = MatrixRow[i][j]

Sum = []

for i in range(size):
    Sum.append(sum(MatrixRow[i]))
    Sum.append(sum(MatrixCol[i]))

if len(set(Sum)) == 1:
    print("magic")
else:
    print("not magic")

# Matrix = []
# FlagRow = False
# FlagCol = False

# for i in range(4):
#     Row = input("").split()
#     for j in range(len(Row)):
#         Row[j] = int(Row[j])
#     Matrix.append(Row)

# if Matrix[0][0] + Matrix[0][1] + Matrix[0][2] + Matrix[0][3] == Matrix[1][0] + Matrix[1][1] + Matrix[1][2] + Matrix[1][3] == Matrix[2][0] + Matrix[2][1] + Matrix[2][2] + Matrix[2][3] == Matrix[3][0] + Matrix[3][1] + Matrix[3][2] + Matrix[3][3]:
#     FlagRow = True
# if Matrix[0][0] + Matrix[1][0] + Matrix[2][0] + Matrix[3][0] == Matrix[0][1] + Matrix[1][1] + Matrix[2][1] + Matrix[3][1] == Matrix[0][2] + Matrix[1][2] + Matrix[2][2] + Matrix[3][2] == Matrix[0][3] + Matrix[1][3] + Matrix[2][3] + Matrix[3][3]:
#     FlagCol = True

# if FlagRow == True and FlagCol == True:
#     print("magic")
# else:
#     print("not magic")