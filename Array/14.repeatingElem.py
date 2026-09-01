arr=[1,1,3,3,2,2,2,4,4,5,6,7]
ans=[]

def repeating(arr):
    hashmap={}
    for i in arr:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    
    
    for key,value in hashmap.items():
        if value>1:
            ans.append(key)
    return ans



print(repeating(arr))

