A_3s = int(input(""))
A_2s = int(input(""))
A_1s = int(input(""))
A_Score = 3*A_3s+2*A_2s+1*A_1s

B_3s = int(input(""))
B_2s = int(input(""))
B_1s = int(input(""))
B_Score = 3*B_3s+2*B_2s+1*B_1s

if A_Score > B_Score:
    print("A")
if A_Score < B_Score:
    print("B")
if A_Score == B_Score:
    print("T")
