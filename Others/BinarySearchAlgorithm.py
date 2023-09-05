X = input("").split(",")

for i in range(len(X)):
    X[i] = int(X[i])
print(X)

Target = int(input(""))
 
# It returns location of x in given array arr
def binarySearch(low, high, target):
    global X
 
    while low <= high:
 
        mid = (low + high) // 2
 
        # Check if x is present at mid
        if X[mid] == target:
            return mid
 
        # If x is greater, ignore left half
        elif X[mid] < target:
            low = mid + 1
 
        # If x is smaller, ignore right half
        else:
            high = mid - 1
 
    # If we reach here, then the element
    # was not present
    return -1
 

    # Function call
result = binarySearch(0, len(X)-1, Target)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
 
    
    
