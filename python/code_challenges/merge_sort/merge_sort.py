

def mergesort(arr):
    n = len(arr)
    
    if n > 1:
        mid =n//2
        
        left=arr[:mid]
        right = arr[mid:]
        # print(right)
        # print(left)
        merge(left, right, arr) 


def merge(left , right , arr):
    '''
    Functions as helper function for merge_sort(), doing the actual
    sorting.
    '''
    i=0
    j=0
    k=0

    while i< len(left) and j< len(right):
        if left[i] <= right[j]:
            arr[k]=left[i]
            i+=1
            
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    if i == len(left):
        for item in right[j:]:
            arr[k]=item
            k+=1
    else:
        for item in left[i:]:
            arr[k] = item
            k += 1        
    
    # print( arr)

print(mergesort([8,4,23,42,16,15]))