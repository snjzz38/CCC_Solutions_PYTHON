C = int(input(""))
List1 = [int(x) for x in input("").split()] 
List2 = [int(x) for x in input("").split()] 

total = 0

if C == 1:
    if List1[0] == 1 and List2[0] == 0:
        total = 3
    elif List1[0] == 0 and List2[0] == 1:
        total = 3
    elif List1[0] == 0 and List2[0] == 0:
        total = 0
    elif List1[0] == 1 and List2[0] == 1:
        total = 4
elif C%2 != 0 and C > 1:
    for i in range(C):
        if List1[i] == 0:
            continue
        else: 
            total += 3
            if i == 0:
                if List1[i+1] == 1:
                    total -= 1
                if List2[i] == 1:
                    total -= 1
            elif (i+1)%2 == 0:
                if List1[i-1] == 1:
                    total -= 1
                if List1[i+1] == 1:
                    total -= 1
            elif i == C-1:
                if List1[i-1] == 1:
                    total -= 1
                if List2[i] == 1:
                    total -= 1
            else:
                if List1[i-1] == 1:
                    total -= 1
                if List1[i+1] == 1:
                    total -= 1
                if List2[i] == 1:
                    total -= 1

    for i in range(C):
        if List2[i] == 0:
            continue
        else: 
            total += 3
            if i == 0:
                if List2[i+1] == 1:
                    total -= 1
                if List1[i] == 1:
                    total -= 1
            elif (i+1)%2 == 0:
                if List2[i-1] == 1:
                    total -= 1
                if List2[i+1] == 1:
                    total -= 1
            elif i == C-1:
                if List2[i-1] == 1:
                    total -= 1
                if List1[i] == 1:
                    total -= 1
            else:
                if List2[i-1] == 1:
                    total -= 1
                if List2[i+1] == 1:
                    total -= 1
                if List1[i] == 1:
                    total -= 1
elif C%2 == 0 and C > 1:
    for i in range(C):
        if List1[i] == 0:
            continue
        else: 
            total += 3
            if i == 0:
                if List1[i+1] == 1:
                    total -= 1
                if List2[i] == 1:
                    total -= 1
            elif (i+1)%2 == 0 and i != C-1:
                if List1[i-1] == 1:
                    total -= 1
                if List1[i+1] == 1:
                    total -= 1
            elif i == C-1:
                if List1[i-1] == 1:
                    total -= 1
            else:
                if List1[i-1] == 1:
                    total -= 1
                if List1[i+1] == 1:
                    total -= 1
                if List2[i] == 1:
                    total -= 1

    for i in range(C):
        if List2[i] == 0:
            continue
        else: 
            total += 3
            if i == 0:
                if List2[i+1] == 1:
                    total -= 1
                if List1[i] == 1:
                    total -= 1
            elif (i+1)%2 == 0 and i != C-1:
                if List2[i-1] == 1:
                    total -= 1
                if List2[i+1] == 1:
                    total -= 1
            elif i == C-1:
                if List2[i-1] == 1:
                    total -= 1
            else:
                if List2[i-1] == 1:
                    total -= 1
                if List2[i+1] == 1:
                    total -= 1
                if List1[i] == 1:
                    total -= 1
else:
    print("error")
             
print(total)