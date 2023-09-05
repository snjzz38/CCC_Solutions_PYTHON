X1 = "YY..Y"
A = [0]*5
for i in range(5):
    if X1[i] == 'Y':
        A[i] = 1
print(A)

X2 = "Y."
B = [0]*5
for i in range(5):
    if X2[i] == 'Y':
        B[i] = 1
print(B)

X3 = ".YY.."
C = [0]*5
for i in range(5):
    if X3[i] == 'Y':
        C[i] = 1
print(C)

for j in range(5):
    print(A[j]+B[j]+C[j])

