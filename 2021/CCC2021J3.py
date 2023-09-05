LastFormulaOdd = True

while True:
    Formula = input("")
    if Formula == "99999":
        break
    Direction = int(Formula[0]) + int(Formula[1])
    TurnVal = Formula[2:]
    if Direction % 2 == 0 and Direction != 0:
        print("right ", end='')
        lastFormulaOdd = False
    elif Direction % 2 == 1:
        print("left ", end='')
        lastFormulaOdd = True
    elif Direction == 0:
        if lastFormulaOdd:
            print("left ", end='')
        else:
            print("right ", end='')
    print(TurnVal)
    


