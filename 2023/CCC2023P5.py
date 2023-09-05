W = input("")
R = int(input(""))
C = int(input(""))

Matrix = []
WordA = []
WordB = []
Slope = []
Level = 0
Num = 0

def valid(Slope):
    global Num
    if len(set(Slope)) <= 1:
        #print("The slope is ", Slope)
        Num += 1
        return True
    elif len(set(Slope)) == 2 and (set(Slope) == {0,2} or set(Slope)=={1,3} or set(Slope)=={2,4} or set(Slope)=={3,5} or set(Slope) == {4,6} or set(Slope)=={5,7} or set(Slope)=={0,6} or set(Slope)=={1,7}):
        #print("the set is ", set(Slope))
        Flag = True
        for i in range(len(W)-2):
            Flag = Flag and Slope[i]<=Slope[i+1]
        if Flag:
            Num += 1
        Flag = True
        for i in range(len(W)-2):
            Flag = Flag and Slope[i]>=Slope[i+1]
        if Flag:
            Num += 1

        return True
    else:
        return False

def findWord(level, a, b):
    global WordA
    global WordB
    global Slope
    if level == len(W):
        valid(Slope)
        return
    elif level > len(W): 
        return
    
    letter = W[level]

    if b<C-1 and Matrix[a][b+1] == letter:
        WordA.append(a)
        WordB.append(b+1)
        Slope.append(0)
        findWord(level+1, a, b+1)
        WordA.pop()
        WordB.pop()
        Slope.pop()

    if a<R-1 and b<C-1 and Matrix[a+1][b+1] == letter:
        WordA.append(a+1)
        WordB.append(b+1)
        Slope.append(1)
        findWord(level+1, a+1, b+1)
        WordA.pop()
        WordB.pop()
        Slope.pop()

    if a<R-1 and Matrix[a+1][b] == letter:
        WordA.append(a+1)
        WordB.append(b)
        Slope.append(2)
        findWord(level+1, a+1, b)
        WordA.pop()
        WordB.pop()
        Slope.pop()

    if a<R-1 and b>0 and Matrix[a+1][b-1] == letter:
        WordA.append(a+1)
        WordB.append(b-1)
        Slope.append(3)
        findWord(level+1, a+1, b-1)
        WordA.pop()
        WordB.pop()
        Slope.pop()

    if b>0 and Matrix[a][b-1] == letter:
        WordA.append(a)
        WordB.append(b-1)
        Slope.append(4)
        findWord(level+1, a, b-1)
        WordA.pop()
        WordB.pop()
        Slope.pop()

    if a>0 and b>0 and Matrix[a-1][b-1] == letter:
        WordA.append(a-1)
        WordB.append(b-1)
        Slope.append(5)
        findWord(level+1, a-1, b-1)
        WordA.pop()
        WordB.pop()
        Slope.pop()

    if a>0 and Matrix[a-1][b] == letter:
        WordA.append(a-1)
        WordB.append(b)
        Slope.append(6)
        findWord(level+1, a-1, b)
        WordA.pop()
        WordB.pop()
        Slope.pop()

    if a>0 and b<C-1 and Matrix[a-1][b+1] == letter:
        WordA.append(a-1)
        WordB.append(b+1)
        Slope.append(7)
        findWord(level+1, a-1, b+1)
        WordA.pop()
        WordB.pop()
        Slope.pop()

    return

for i in range(R):
    Matrix.append(input("").split(" "))

for i in range(R):
    for j in range(C):
        if Matrix[i][j] == W[0]:
            WordA.append(i)
            WordB.append(j)
            findWord(1, i, j)
            WordA.pop()
            WordB.pop()

print(Num)