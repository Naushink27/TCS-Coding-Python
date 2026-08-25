arr=[1,2,3,4,5,6,7,8,9,10]
k=5

# right: [4,5,1,2,3]

# reverse array:[5,4,3,2,1]
# reverse k :[4,5,3,2,1]
#reverse after k:[4,5,1,2,3]

def Reverse(arr,s,e):
    while s<e:
        [arr[s],arr[e]]=[arr[e],arr[s]]
        s=s+1
        e=e-1
    


    


def reversed(arr,k):
    Reverse(arr,0,len(arr)-1)
    Reverse(arr,0,k-1)
    Reverse(arr,k,len(arr)-1)

    return arr


print(reversed(arr,k))
