arr=[1,2,4,52,6,73,8,9,3]



def min(arr):
    min=float('inf')
    for i in arr:
        if i<min:
            min=i
    
    return min

print(min(arr))

    


