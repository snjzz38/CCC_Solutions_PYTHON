N = int(input(""))
List = []

for i in range(N):
    List.append(int(input("")))
List.sort()

PointsList = []
for i in range(len(List)-2):
    A = (List[i+1]-List[i])/2
    B = (List[i+2]-List[i+1])/2
    S = A+B
    PointsList.append(S)
PointsList.sort()
print(PointsList[0])



