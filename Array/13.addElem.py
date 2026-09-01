arr=[1,2,3,4,5,6]

def insertAtBegin(num):
    arr.insert(0,num)

def insertAtEnd(num):
    arr.insert(len(arr),num)

def insertAtIndx(num,indx):
    arr.insert(indx,num)


insertAtBegin(80)
insertAtEnd(6)
insertAtIndx(78,5)


print(arr)