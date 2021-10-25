# Merge Sort

def mergeSort(arr,l,r):
    middle = l + (r-l)/2
    l =arr[:mid] 
    r =arr[mid:]
    
    mergeSort(l)
    
    mergeSort(r)
    
    # Merge the sorted array
    i = j = k = 0
    while i <len(l) and j <len(r):
        if(l[i] < r[j]):
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k +=1
            
        
        

    
    
