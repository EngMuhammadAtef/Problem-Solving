def MergeSort(arr):
    if len(arr) > 1: # if len = 1 is mean it is a sorted array
        # get Mid to divide problem to subproblems (divide and conquer)
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        # divide left to become one element in array
        MergeSort(L) 

        # divide right to become one element in array
        MergeSort(R) 

        # intiate 3 indexes
        i = j = k = 0 

        # compare Left elements to Right elements
        while i<len(L) and j<len(R): # R[1,3] L[2,4,5] i=2 j=1 and arr[3,1,4,2,5] k=4 ==> arr[1,2,3]
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        # to empty Left[] all greater elements that pionter not get it in first (while)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        # to empty Right[] all greater elements that pionter not get it in first (while)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [10,9,8,7,6,0,5,4,3,2,1]
MergeSort(arr)
print(arr)

