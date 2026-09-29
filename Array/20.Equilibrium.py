# The equilibrium index of an array is an index such that the sum of elements at lower indices is equal to the sum of elements at higher indices.
# In other words, the total sum of everything to the left of the index must equal the total sum of everything to the right of it.


arr=[-7, 1, 5, 2, -4, 3, 0]

total_sum=sum(arr)

leftSum=0

for i in range (len(arr)):
    rightSum=total_sum-leftSum-arr[i]

    if leftSum==rightSum:
        print(i)
        break;
    
    leftSum+=arr[i]

print(-1)
