
arr=[1,3,1,4,3,4,1,5,6,5,5,6,7,7,7]

def frequency(arr):
    freq_Map = {}

    for i in arr:
        freq_Map[i]=(freq_Map.get(i)or 0)+1
        
    
    for key,value in freq_Map.items():
        print(key,value)
    

frequency(arr)