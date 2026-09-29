import heapq

def kthLargestElem(arr,k):
    heap=[]
    for num in arr:
        heapq.heappush(heap,num)
        if len(heap)>k:
            heapq.heappop(heap)
    
    return heap[0]

print(kthLargestElem([3, 2, 1, 5, 6, 4], 2))  # Outputs: 5