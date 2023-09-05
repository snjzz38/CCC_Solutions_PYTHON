X = int(input(""))

myList = []
myResult = []
for i in range(X):
    a = input("")
    myList.append(a)

for i in range(5):
    total = 0
    for j in range(len(myList)):
        if myList[j][i] == "Y":
            total += 1
    myResult.append(total)
    
myIndex = []
for i in range(len(myResult)):
    if myResult[i] == max(myResult):
        myIndex.append(i+1)
        
print(*myIndex, sep=',')