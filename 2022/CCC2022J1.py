LBox = int(input(""))
SBox = int(input(""))
C = LBox*8+SBox*3

if C<28:
    print("C must be more than 28")
else:
    print(C-28)