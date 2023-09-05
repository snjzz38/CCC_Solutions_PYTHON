def absolute_value(x, y):
    if x-y >= 0:
        return x-y
    else:
        return y-x 

AB = input("")
CD = input("")
Battery = int(input(""))
ListAB = AB.split()
ListCD = CD.split()
Xdiff = (absolute_value(int(ListAB[0]), int(ListCD[0])))
Ydiff = (absolute_value(int(ListAB[1]), int(ListCD[1])))
Remaining = Battery-Xdiff-Ydiff

if Remaining % 2 == 0 and Battery > Xdiff+Ydiff or Remaining == 0:
    print("Y")
elif Remaining % 2 != 0 and Battery > Xdiff+Ydiff:
    print("N")

if Battery < Xdiff+Ydiff:
    print("N")
