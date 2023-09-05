n = int(input(""))
t = int(input(""))
yard = [[0 for col in range(n)] for row in range(n)]
trees = []
pool_size = n-1

for i in range(t):
    location_in = input("").split(' ')
    loc_x = int(location_in[0]) - 1
    loc_y = int(location_in[1]) - 1 
    trees.append([loc_x, loc_y])
    yard[loc_x][loc_y] = 1

def check_has_tree(in_size, in_row, in_col):
    global trees
    for tree in trees:
        if in_row <= tree[0] <= in_row + in_size - 1 and in_col <= tree[1] <= in_col + in_size - 1:
            return True
    return False

def check(in_size, in_row, in_col):
    for i in range(n - in_size + 1):
        for j in range(n - in_size + 1): 
            has_trees = check_has_tree(in_size, in_row + i, in_col + j)
            if not has_trees:
                return True
    return False     

# It returns location of x in given array arr
def binarySearch(low, high):
    global yard
 
    while low <= high:
        mid = (low + high) // 2
 
        # if we can find a pool size of mid
        if check(mid, 0, 0):
            low = mid + 1
 
        # If x is greater, ignore left half
        else:
            high = mid - 1
 
    # If we reach here, then the element
    # was not present
    return low-1

checked = False
pool_size = binarySearch(1, n)

print(pool_size)