def insert_ShiftArray(arr , x):
    num = len(arr)//2
    arr.insert(num , x)
    return arr 
    
   



print(insert_ShiftArray([1,2,3,5,6,7,0,7] , 9))
