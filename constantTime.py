#=======================================
def addItems(n):
    sum = n + n
    print(sum)

addItems(10)


#=======================================

def findNum(A, index):
    if 0 <= index < len(A):
        return A[index]
    else:
        return "Index out of range"

A = [40,30,60, 50]
result = findNum(A, 2)
print(result)
    

    
    
