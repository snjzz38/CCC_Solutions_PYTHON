T = input("")
S = input("")

X = T.count(S)
print(X)

start = 0

for i in range(X):
    Y = T.index(S, i)
    if i == 0:
        start = T.index(S, start)
        print(start)
    else:
        start = T.index(S, start+len(S))
        print(start)
    