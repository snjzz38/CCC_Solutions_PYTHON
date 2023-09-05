n = int(input(""))
t = int(input(""))
yard = [[0 for col in range(n)] for row in range(n)] 
m = 0
max_m = 0

for i in range(t):
    tree = input("").split(' ')
    loc_row = int(tree[0]) - 1
    loc_col = int(tree[1]) - 1
    yard[loc_row][loc_col] = 1

def exterior(start_row, start_col, size):
    global yard 
    qualified = True 
    for i in range(size):
        if start_row + size - 1 > n - 1 or start_col + size - 1 > n - 1:
            qualified = False
            break
        if yard[start_row + i][start_col + size - 1] == 1:
            qualified = False
            break
        if yard[start_row + size - 1][start_col + i] == 1:
            qualified = False
            break
    if qualified:
        return exterior(start_row, start_col, size + 1)
    else:
        return size - 1
    
for i in range(n):
    for j in range(n):
        if yard[i][j] == 1:
            break
        else:
            m = exterior(i, j, 2)
            if m > max_m:
                max_m = m 

print(max_m)
    

    

