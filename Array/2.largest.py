arr=[1,3,5,7,8,8,99,67,46,356,3456]

def largest(arr):
    max=float('-inf')

    for i in arr:
        if i>max:
            max=i
        
    return max

print(largest(arr))
print(max(arr))