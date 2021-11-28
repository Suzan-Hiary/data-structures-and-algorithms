def insertion_Sort(array):
    for i in range(len(array)):
        j = i -1 
        temp = array[i]

        while j >= 0 and temp < array[j] :
            array[j+1] = array[j]   
            j-=1

        array[j+1] = temp
        print(array)
    return array

arr=[20,18,12,8,5,-2]

insertion_Sort(arr)        


