s = input("")
catchnum = False
numstr = ""

for i in range(len(s)):
    char = s[i]
    if char.isalpha():
        if catchnum:
            print(numstr)
            catchnum = False
            numstr = ""
        print(char, end='')
    elif char.isdigit():
        numstr += char
        if i == len(s)-1:
            print(numstr)
    elif char == "+":
        catchnum = True
        print(" tighten ", end='')
    elif char == "-":
        catchnum = True
        print(" loosen ", end='')
    else:
        print("error")



