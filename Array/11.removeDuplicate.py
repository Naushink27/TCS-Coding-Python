arr=[1,1,2,3,3,4,5,5,6,7,7,7,8,9]

x=0

for i in range(0,len(arr)):
    if(arr[i]!=arr[x]):
        x=x+1
        arr[x]=arr[i]


print(x+1)
print(arr)



