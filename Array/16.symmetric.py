arr=[(1,2),(2,1),(3,4),(4,5),(5,4)]


def symmetric(arr):
    hashmap={}

    for i in range(len(arr)):
        first,second=arr[i]

        if second in hashmap and hashmap[second]==first:
              print(f"({first} {second})", end=" ")
        else:
            hashmap[first]=second

        
symmetric(arr)
