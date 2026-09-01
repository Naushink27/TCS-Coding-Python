arr=[1,2,-3,0,-4,-5]

def maxProduct(arr):
    maxProduct=1
    curr=1

    for i in range(len(arr)):
        curr=curr* arr[i]

        maxProduct=max(maxProduct,curr)
    return maxProduct

print(maxProduct(arr))



