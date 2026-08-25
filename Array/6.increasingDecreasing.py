arr=[4, 2, 8 ,6 ,15, 5 ,9 ,20]

# output: [2 4 5 6 20 15 9 8]
# sort: 2,4,5,6,8,9,15,20
arr.sort()

def rearrange(arr):
    n=len(arr)
    arr[n//2:]=reversed(arr[n//2:])
    return arr


print(rearrange(arr))

