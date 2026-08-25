def secondLargest(arr):
    first=float('-inf')
    sec=float('-inf')
    for i in arr:
        if i>first:
            sec=first
            first=i
        elif i>sec  and i!=sec:
            sec=i
    
    return sec


print(secondLargest([1,2,4,5,7,8,9]))

def secondSmallest(arr):
    first=float('inf')
    second=float('inf')

    for i in arr:
        if i<first:
            sec=first
            first=i
        
        elif i<sec and i!=sec:
            sec=i
        
    
    return sec

print(secondSmallest([1,2,4,6,778,9,6,5]))





