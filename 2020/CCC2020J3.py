Drops = int(input(""))
XCoordinateList = []
YCoordinateList = []

for i in range(Drops):
    Droplet = input("").split(",")
    X = Droplet[0]
    Y = Droplet[1]
    XCoordinateList.append(X)
    YCoordinateList.append(Y)

Max_X = int(max(XCoordinateList))+1
Min_X = int(min(XCoordinateList))-1
Max_Y = int(max(YCoordinateList))+1
Min_Y = int(min(YCoordinateList))-1

print(Min_X, ",", Min_Y, sep='')
print(Max_X, ",", Max_Y, sep='')

# print(min(XCoordinateList[X+1]), ",", min(YCoordinateList[Y+1]), sep='')
# print(max(XCoordinateList[X-1]), ",", min(YCoordinateList[Y-1]), sep='')

# 5
# 44,62
# 34,69
# 24,78
# 42,44
# 64,10