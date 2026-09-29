def isAbundant(num):
    div_sum=0

    for i in range (1,num//2+1):
        if num%i==0:
            div_sum+=i
        
    return div_sum>num


print(isAbundant(12))
