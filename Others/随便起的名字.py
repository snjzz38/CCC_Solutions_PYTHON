Word = input("")
H = int(input(""))
V = int(input(""))
GridH = []
GridV = []
Total = 0

for i in range(H):
    GridH.append(input("").replace(" ", ""))

def CheckH():
    global GridH
    global Total
    for i in range(H):
        if Word in GridH[i] or Word[::-1] in GridH[i]:
            Total += 1

def CheckV():
    global GridV
    global GridH
    global Total
    for i in range(V):
        Text = ""
        for j in range(H):
            Text += GridH[j][i]
        GridV.append(Text)
    for i in range(V):
        if Word in GridV[i] or Word[::-1] in GridV[i]:
            Total += 1
    

CheckH()
CheckV()
print(Total)


# MENU
# 5
# 7
# F T R U B L K
# P M N A X C U
# A E R C N E O
# M N E U A R M
# M U N E M N S