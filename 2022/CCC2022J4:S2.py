Xnames = {}
Ynames = {}
Gnames = []

X = int(input(""))
if X>0:
    for i in range(X):
        Value = input("").split()
        Key = Value[0]+'-'+Value[1]
        Xnames[Key] = Value

Y = int(input(""))
if Y>0:
    for i in range(Y):
        Value = input("").split()
        Key = Value[0]+'-'+Value[1]
        Ynames[Key] = Value

G = int(input(""))
if G>0:
     for i in range(G):
        Gnames.append(input("").split()) 

Total = 0  

for i in range(G):
    if X>0:
        for j in range(len(Xnames)):
            if Xnames[j][0] in Gnames[i] and Xnames[j][1] not in Gnames[i]:
                Total +=1
            if Xnames[j][1] in Gnames[i] and Xnames[j][0] not in Gnames[i] and FlagX[j] == 0:
                Total += 1
            
    if Y>0:
        for j in range(Y):
            if Ynames[j][0] in Gnames[i] and Ynames[j][1] in Gnames[i] and FlagY[j] == 0:
                FlagY[j] = 1
                Total += 1 
print(Total)