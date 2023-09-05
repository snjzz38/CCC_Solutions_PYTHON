N = int(input(""))
K = int(input(""))
List = []
Total = 0

for i in range(K):
    List.append(K-i)

for i in range(K):
    Total += N*(10**List[i])
Total += N
print(Total)