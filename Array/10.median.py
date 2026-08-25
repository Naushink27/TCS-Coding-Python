arr = [4, 7, 1, 2, 5, 6]


def median(arr):
    arr.sort()
    n=len(arr)
    if n%2==0:
        indx1=arr[n//2-1]
        indx2=arr[n//2]
        return (indx1+indx2)/2
    else:
        return arr[n//2]
    

print(median(arr))