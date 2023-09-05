x = float(input("Set X to: "))
y = float(input("Set Y to: "))

opr = 0
opr = int(input("Choose the operation: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for exponents, 6 for square roots. Press anything else to exit: "))
if opr == 1:
    print("x+y = ", x+y)
elif opr == 2:
    print("x-y = ", x-y)
elif opr == 3:
    print("x*y = ", x*y)
elif opr == 4:
    print("x/y = ", x/y)
elif opr == 5:
    print("x^y = ", x**y)
elif opr == 6:
    print("x^(1/y) = ", x**(1/y))
else:
    print("Restart the code.") 