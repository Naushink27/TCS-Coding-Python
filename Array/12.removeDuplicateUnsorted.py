arr = [4, 5, 4, 2, 2, 3, 1]

def removeDuplicate(arr):
    map={}
    res=[]
    for i in arr:
        if i not in map:
            res.append(i)
            map[i]=True
        

    return res
    

print(removeDuplicate(arr))