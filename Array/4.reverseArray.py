arr=[1,2,3,4,5,6,7,8]

def reverse(arr):
    n=len(arr)
    mid=len(arr)//2
    for i in range(0,mid):
        temp=arr[i]
        arr[i]=arr[n-i-1]
        arr[n-i-1]=temp
    
    return arr

print(reverse(arr))