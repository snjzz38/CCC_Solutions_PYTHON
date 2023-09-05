T = input("")
S = input("")
List = []
flag = False

for i in range(len(S)):
    X = S[i:]+S[0:i]
    List.append(X)
    
for i in range(len(S)):
    if List[i] in T:
        print("yes")
        flag = True
        break

if not flag:
    print("no")
        