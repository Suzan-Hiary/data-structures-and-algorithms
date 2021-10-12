def array_sheft(arr,n):
    for i in range(len(arr)) :
        if arr[i] > n :
            i = i
            break
    arr = arr[:i] + [n] +arr[i:]     
    return arr

print(array_sheft([3,4,6,8],5))
    
   




