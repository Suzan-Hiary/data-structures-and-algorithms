def BinarySearch(k , list): 
  L = 0
  R= len(list)-1
  found= False

  while   L <= R and found== False : 
     middle_index= (L+R)//2
     if list[middle_index] == k :
       found= True 
       return middle_index 
       

     else :
        if list[middle_index] < k :
           L= middle_index +1 
        else:
          R = middle_index -1 
  if found == True :
    return middle_index
  else:
    return -1   



print(BinarySearch(5, [1,2,3,4,5,6,7]))